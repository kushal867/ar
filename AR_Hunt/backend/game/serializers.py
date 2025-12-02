from rest_framework import serializers
from .models import POI, Participant, Progress


class POIListSerializer(serializers.ModelSerializer):
    """Serializer for listing POIs - hides secret word"""
    class Meta:
        model = POI
        fields = ['id', 'name', 'description', 'lat', 'lon', 'sequence_order', 'icon']


class POIDetailSerializer(serializers.ModelSerializer):
    """Serializer for POI details - includes secret word after unlock"""
    class Meta:
        model = POI
        fields = ['id', 'name', 'description', 'lat', 'lon', 'sequence_order', 'icon', 'secret_word', 'qr_code_url']


class ParticipantSerializer(serializers.ModelSerializer):
    progress_count = serializers.ReadOnlyField()
    time_elapsed = serializers.ReadOnlyField()
    
    class Meta:
        model = Participant
        fields = ['id', 'device_id', 'name', 'email', 'start_time', 'completed_at', 
                  'is_completed', 'progress_count', 'time_elapsed']
        read_only_fields = ['start_time', 'completed_at', 'is_completed']


class ProgressSerializer(serializers.ModelSerializer):
    poi_name = serializers.CharField(source='poi.name', read_only=True)
    poi_icon = serializers.CharField(source='poi.icon', read_only=True)
    
    class Meta:
        model = Progress
        fields = ['id', 'poi', 'poi_name', 'poi_icon', 'found_at', 'submitted_word']
        read_only_fields = ['found_at']


class SubmitWordSerializer(serializers.Serializer):
    """Serializer for submitting a secret word"""
    participant_id = serializers.CharField(max_length=255)
    secret_word = serializers.CharField(max_length=100)
    
    def validate(self, data):
        # Check if participant exists
        try:
            participant = Participant.objects.get(device_id=data['participant_id'])
        except Participant.DoesNotExist:
            raise serializers.ValidationError("Participant not found. Please register first.")
        
        data['participant'] = participant
        return data
