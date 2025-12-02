from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import POIViewSet, ParticipantViewSet, GameStatusView

router = DefaultRouter()
router.register(r'poi', POIViewSet, basename='poi')
router.register(r'participants', ParticipantViewSet, basename='participant')

urlpatterns = [
    path('', include(router.urls)),
    path('game/status/', GameStatusView.as_view({'get': 'status'}), name='game-status'),
    path('game/final/', GameStatusView.as_view({'get': 'final'}), name='game-final'),
]
