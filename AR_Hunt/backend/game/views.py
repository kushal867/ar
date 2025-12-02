from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.utils import timezone
from .models import POI, Participant, Progress
from .serializers import (
    POIListSerializer, POIDetailSerializer, 
    ParticipantSerializer, ProgressSerializer,
    SubmitWordSerializer
)


class POIViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet for POI endpoints
    - list: Returns all POIs (without secret words)
    - retrieve: Returns single POI details
    - qr: Returns QR code for a POI
    - submit: Submit secret word for a POI
    """
    queryset = POI.objects.all()
    
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return POIDetailSerializer
        return POIListSerializer
    
    @action(detail=True, methods=['get'])
    def qr(self, request, pk=None):
        """Get QR code URL for a POI"""
        poi = self.get_object()
        
        # Generate QR code URL if not set
        if not poi.qr_code_url:
            # Using QR Server API
            qr_data = f"POI:{poi.id}|{poi.name}"
            poi.qr_code_url = f"https://api.qrserver.com/v1/create-qr-code/?size=300x300&data={qr_data}"
            poi.save()
        
        return Response({
            'poi_id': poi.id,
            'name': poi.name,
            'qr_code_url': poi.qr_code_url,
            'sequence_order': poi.sequence_order
        })
    
    @action(detail=True, methods=['post'])
    def submit(self, request, pk=None):
        """Submit secret word for a POI"""
        poi = self.get_object()
        serializer = SubmitWordSerializer(data=request.data)
        
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        participant = serializer.validated_data['participant']
        secret_word = serializer.validated_data['secret_word']
        
        # Check if already found
        if Progress.objects.filter(participant=participant, poi=poi).exists():
            return Response({
                'success': False,
                'message': 'You have already found this POI.'
            }, status=status.HTTP_400_BAD_REQUEST)
        
        # Check sequence - must complete previous POIs first
        if poi.sequence_order > 1:
            previous_poi = POI.objects.filter(sequence_order=poi.sequence_order - 1).first()
            if previous_poi and not Progress.objects.filter(participant=participant, poi=previous_poi).exists():
                return Response({
                    'success': False,
                    'message': f'You must complete "{previous_poi.name}" first.',
                    'required_poi': previous_poi.name
                }, status=status.HTTP_400_BAD_REQUEST)
        
        # Validate secret word (case-insensitive)
        if secret_word.strip().lower() != poi.secret_word.strip().lower():
            return Response({
                'success': False,
                'message': 'Incorrect secret word. Try again.'
            }, status=status.HTTP_400_BAD_REQUEST)
        
        # Create progress record
        progress = Progress.objects.create(
            participant=participant,
            poi=poi,
            submitted_word=secret_word
        )
        
        # Check if all POIs completed
        total_pois = POI.objects.count()
        completed_pois = Progress.objects.filter(participant=participant).count()
        
        if completed_pois == total_pois:
            participant.is_completed = True
            participant.completed_at = timezone.now()
            participant.save()
        
        return Response({
            'success': True,
            'message': f'Correct! You found {poi.name}.',
            'poi': POIDetailSerializer(poi).data,
            'progress': {
                'found': completed_pois,
                'total': total_pois,
                'completed': participant.is_completed
            }
        }, status=status.HTTP_201_CREATED)


class ParticipantViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Participant endpoints
    - create: Register a new participant
    - retrieve: Get participant details
    """
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer
    lookup_field = 'device_id'


class GameStatusView(viewsets.ViewSet):
    """
    Game status endpoints
    - status: Get participant progress
    - final: Check if participant can access final form
    """
    
    @action(detail=False, methods=['get'])
    def status(self, request):
        """Get game status for a participant"""
        device_id = request.query_params.get('device_id')
        
        if not device_id:
            return Response({
                'error': 'device_id parameter required'
            }, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            participant = Participant.objects.get(device_id=device_id)
        except Participant.DoesNotExist:
            return Response({
                'error': 'Participant not found. Please register first.'
            }, status=status.HTTP_404_NOT_FOUND)
        
        # Get progress
        progress = Progress.objects.filter(participant=participant).select_related('poi')
        found_pois = [p.poi for p in progress]
        
        # Get next POI
        next_poi = None
        all_pois = POI.objects.all()
        for poi in all_pois:
            if poi not in found_pois:
                next_poi = poi
                break
        
        return Response({
            'participant': ParticipantSerializer(participant).data,
            'found_pois': POIListSerializer(found_pois, many=True).data,
            'next_poi': POIListSerializer(next_poi).data if next_poi else None,
            'progress': {
                'found': len(found_pois),
                'total': all_pois.count(),
                'completed': participant.is_completed
            }
        })
    
    @action(detail=False, methods=['get'])
    def final(self, request):
        """Check if participant can access final submission"""
        device_id = request.query_params.get('device_id')
        
        if not device_id:
            return Response({
                'error': 'device_id parameter required'
            }, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            participant = Participant.objects.get(device_id=device_id)
        except Participant.DoesNotExist:
            return Response({
                'error': 'Participant not found'
            }, status=status.HTTP_404_NOT_FOUND)
        
        if not participant.is_completed:
            remaining = POI.objects.count() - Progress.objects.filter(participant=participant).count()
            return Response({
                'unlocked': False,
                'message': f'Complete all {remaining} remaining POIs to unlock final submission.',
                'remaining': remaining
            })
        
        return Response({
            'unlocked': True,
            'message': 'Congratulations! You can now submit your final form.',
            'google_form_url': 'https://forms.google.com/your-form-link',  # Update with actual URL
            'completion_time': participant.time_elapsed
        })
