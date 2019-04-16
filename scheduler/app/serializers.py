from .models import Appointment, Patient, Procedure

from rest_framework import serializers

class PatientSerializer(serializers.ModelSerializer):
    """ Patient model serializer """

    class Meta:
        model = Patient
        fields = ("id", "name", "birthdate", "sex", "phone", "email")
        read_only_fields = ("id",)

class ProcedureSerializer(serializers.ModelSerializer):
    """ Procedure model serializer """

    class Meta:
        model = Procedure
        fields = ("id", "description", "cost")

class AppointmentSerializer(serializers.ModelSerializer):
    """ Appointment model serializer """

    patient = PatientSerializer
    procedure = ProcedureSerializer
    read_only_fields = ("id")

    class Meta:
        model = Appointment
        fields = ("id", "patient", "procedure", "date", "start_at", "end_at")
