from rest_framework.test import APITransactionTestCase

from app.models import Appointment

class AppointmentTestCase(APITransaction):
    """ Test cases for the Appointment API """

    def setUp(self):

        Appointment.objects.create(
            patient="Vinicius Chan",
            procedure="Consulta",
            date="2017-12-12",
            start_at="08:00",
            end_at="09:00"
        )

        Appointment.objects.create(
            patient="Erika Correa",
            procedure="Exame",
            date="2017-12-20",
            start_at="15:00",
            end_at="18:00"
        )