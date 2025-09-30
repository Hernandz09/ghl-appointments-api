from django.contrib import admin
from .models import Appointment

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('ghl_id', 'title', 'appointment_status', 'start_time', 'end_time')
    list_filter = ('appointment_status', 'start_time')
    search_fields = ('ghl_id', 'title', 'contact_id')
    readonly_fields = ('ghl_id', 'date_added', 'date_updated')
