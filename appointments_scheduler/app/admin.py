from django.contrib import admin
from .models import Appointment, Patient, Procedure


class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['patient', 'procedure', 'date', 'start_at', 'end_at']


class PatientAdmin(admin.ModelAdmin):
    list_display = ['name', 'sex', 'birthdate', 'phone', 'email']


class ProcedureAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'cost']


admin.site.register(Appointment, AppointmentAdmin)
admin.site.register(Patient, PatientAdmin)
admin.site.register(Procedure, ProcedureAdmin)
