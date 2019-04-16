from datetime import date

from .models import Appointment, Patient, Procedure

from rest_framework import serializers


class PatientSerializer(serializers.ModelSerializer):
    """ Patient model serializer """

    class Meta:
        model = Patient
        fields = ('id', 'name', 'birthdate', 'sex', 'phone', 'email')
        read_only_fields = ('id',)

    def validate_name(self, value):
        if not len(value.split()) > 1:
            raise serializers.ValidationError('Not a valid name')
        return value

    def validate_phone(self, value):
        if not len(value) >= 10:
            raise serializers.ValidationError('Not a valid number')
        return value


class ProcedureSerializer(serializers.ModelSerializer):
    """ Procedure model serializer """

    class Meta:
        model = Procedure
        fields = ('id', 'description', 'cost')

    def validate_cost(self, value):
        if value < 0:
            raise serializers.ValidationError('Not a valid price')
        return value


class AppointmentSerializer(serializers.ModelSerializer):
    """ Appointment model serializer """

    patient = PatientSerializer
    procedure = ProcedureSerializer
    read_only_fields = ('id')

    class Meta:
        model = Appointment
        fields = ('id', 'patient', 'procedure', 'date', 'start_at', 'end_at')

    def validate_date(self, value):
        today = date.today()
        if value < today:
            raise serializers.ValidationError(
                'Not allowed to create appointments in the past'
            )
        return value
