from rest_framework.test import APITransactionTestCase

from .models import Patient

class PatientTestCase(APITransactionTestCase):
    """ Test cases for patient API """

    def setUp(self):

        Patient.objects.create(
            id=1,
            name="Test User",
            birthdate="1995-12-09",
            sex="F",
            phone="16998882809",
            email="test2@email.com"
        )

        Patient.objects.create(
            id=2,
            name="Michael William",
            birthdate="2017-12-10",
            sex="F",
            phone="16923232323",
            email="michael@hotmail.com"
        )


    def test_patient_list(self):
        
        response = self.client.get("/patients/")
        
        self.assertEqual(response.json(),
            [
                {
                    "id": 1,
                    "name": "Test User",
                    "birthdate": "1995-12-09",
                    "sex": "F",
                    "phone": "16998882809",
                    "email": "test2@email.com"
                },
                {
                    "id": 2,
                    "name": "Michael William",
                    "birthdate": "2017-12-10",
                    "sex": "F",
                    "phone": "16923232323",
                    "email": "michael@hotmail.com"
                }
            ]
        )

        self.assertEqual(response.status_code, 200)

    def test_patient_create(self):
        
        payload = {
            "id": 1,
            "name": "Test User",
            "birthdate": "1995-12-09",
            "sex": "F",
            "phone": "16998882809",
            "email": "test2@email.com"
        }

        response = self.client.post("/patients/", payload)
        self.assertEqual(response.status_code, 201)


    def test_patient_delete(self):
        response = self.client.delete("/patients/1/")
        self.assertEqual(response.status_code, 204)


