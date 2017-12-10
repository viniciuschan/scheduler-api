from rest_framework.test import APITransactionTestCase

from app.models import Patient

class PatientTestCase(APITransactionTestCase):
    """ Test cases for patient API """

    def setUp(self):

        Patient.objects.create(
            id=1,
            name="Vinicius Chan",
            birthdate="1990-09-07",
            sex="M",
            phone="16981211201",
            email="viniciuschan@hotmail.com"
        )

        Patient.objects.create(
            id=2,
            name="Marcela Correa",
            birthdate="1996-11-05",
            sex="F",
            phone="16982827373",
            email="marcela@hotmail.com"
        )