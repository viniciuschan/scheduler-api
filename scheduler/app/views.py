from rest_framework import viewsets

from .models import Appointment, Patient, Procedure
from .serializers import (
    AppointmentSerializer,
    PatientSerializer,
    ProcedureSerializer,
)


class AppointmentViewSet(viewsets.ModelViewSet):
    """ API endpoint that allows appointments to be viewed or edited. """

    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

class PatientViewSet(viewsets.ModelViewSet):
    """ API endpoint that allows patients to be viewed or edited. """

    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class ProcedureViewSet(viewsets.ModelViewSet):
    """ API endpoint that allows procedures to be viewed or edited. """

    queryset = Procedure.objects.all()
    serializer_class = ProcedureSerializer
