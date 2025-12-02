from django.contrib import admin
from .models import POI, Participant, Progress


@admin.register(POI)
class POIAdmin(admin.ModelAdmin):
    list_display = ['sequence_order', 'name', 'secret_word', 'lat', 'lon']
    list_editable = ['secret_word']
    ordering = ['sequence_order']
    search_fields = ['name', 'secret_word']


@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ['device_id', 'name', 'start_time', 'progress_count', 'is_completed']
    list_filter = ['is_completed', 'start_time']
    search_fields = ['device_id', 'name', 'email']
    readonly_fields = ['start_time', 'completed_at', 'progress_count', 'time_elapsed']


@admin.register(Progress)
class ProgressAdmin(admin.ModelAdmin):
    list_display = ['participant', 'poi', 'found_at', 'submitted_word']
    list_filter = ['poi', 'found_at']
    search_fields = ['participant__name', 'participant__device_id', 'poi__name']
    readonly_fields = ['found_at']
