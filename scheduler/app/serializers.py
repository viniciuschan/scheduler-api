from datetime import date

from rest_framework import serializers

from .models import Appointment, Patient, Procedure

class PatientSerializer(serializers.ModelSerializer):
    """ Patient model serializer """

    class Meta:
        model = Patient
        fields = ('id', 'name', 'birthdate', 'sex', 'phone', 'email')

    def validate_name(self, value):
        if not len(value) > 1:
            raise serializers.ValidationError('Not a valid patient name')
        return value

    def validate_phone(self, value):
        if len(value) < 9 or len(value) > 12:
            raise serializers.ValidationError('Not a valid phone number')
        return value


class ProcedureSerializer(serializers.ModelSerializer):
    """ Procedure model serializer """

    class Meta:
        model = Procedure
        fields = ('id', 'description', 'cost')

    def validate_cost(self, value):
        if value < 0:
            raise serializers.ValidationError('Not a valid procedure price')
        return value


class AppointmentSerializer(serializers.ModelSerializer):
    """ Appointment model serializer """

    # patient = PatientSerializer()
    # procedure = ProcedureSerializer()

    class Meta:
        model = Appointment
        fields = ('id', 'patient', 'procedure', 'date', 'start_at', 'end_at')

    def validate_date(self, value):
        if value <= date.today():
            raise serializers.ValidationError(
                'Not allowed to create appointments in the past'
            )
        return value
