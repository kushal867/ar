from django.db import models
from django.utils import timezone


class POI(models.Model):
    """Point of Interest - represents a checkpoint in the AR hunt"""
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    lat = models.FloatField(help_text="Latitude coordinate")
    lon = models.FloatField(help_text="Longitude coordinate")
    secret_word = models.CharField(max_length=100, help_text="Secret keyword to unlock")
    sequence_order = models.IntegerField(unique=True, help_text="Order in which POI must be visited (1-6)")
    icon = models.CharField(max_length=10, default='📍')
    qr_code_url = models.URLField(blank=True, help_text="URL for QR code image")
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['sequence_order']
        verbose_name = "Point of Interest"
        verbose_name_plural = "Points of Interest"
    
    def __str__(self):
        return f"{self.sequence_order}. {self.name}"


class Participant(models.Model):
    """Represents a player in the AR hunt"""
    device_id = models.CharField(max_length=255, unique=True, help_text="Unique device identifier")
    name = models.CharField(max_length=200, blank=True)
    email = models.EmailField(blank=True)
    start_time = models.DateTimeField(default=timezone.now)
    completed_at = models.DateTimeField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.name or self.device_id}"
    
    @property
    def progress_count(self):
        """Returns number of POIs found"""
        return self.progress_set.count()
    
    @property
    def time_elapsed(self):
        """Returns time elapsed in minutes"""
        if self.completed_at:
            delta = self.completed_at - self.start_time
        else:
            delta = timezone.now() - self.start_time
        return delta.total_seconds() / 60


class Progress(models.Model):
    """Tracks which POIs a participant has found"""
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    poi = models.ForeignKey(POI, on_delete=models.CASCADE)
    found_at = models.DateTimeField(default=timezone.now)
    submitted_word = models.CharField(max_length=100, help_text="Word submitted by participant")
    
    class Meta:
        ordering = ['found_at']
        unique_together = ['participant', 'poi']
        verbose_name_plural = "Progress"
    
    def __str__(self):
        return f"{self.participant} - {self.poi.name}"
