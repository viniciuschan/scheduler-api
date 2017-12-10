from rest_framework.test import APITransactionTestCase

from .models import Patient, Procedure, Appointment

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


    def test_patient_detail(self):
    
        response = self.client.get("/patients/1/")

        self.assertDictEqual(response.json(),
            {
                "id": 1,
                "name": "Test User",
                "birthdate": "1995-12-09",
                "sex": "F",
                "phone": "16998882809",
                "email": "test2@email.com"
            }
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


class ProcedureTestCase(APITransactionTestCase):
    """ Tese cases for the procedure API """
    def setUp(self):

        Procedure.objects.create(
            id=1,
            description="Consulta",
            cost="100.00"
        )

        Procedure.objects.create(
            id=2,
            description="Exame",
            cost="200.00"
        )


    def test_procedures_list(self):

        response = self.client.get("/procedures/")

        self.assertEqual(response.json(),
            [
                {
                    "id": 1,
                    "description": "Consulta",
                    "cost": "100.00"
                },
                {
                    "id": 2,
                    "description": "Exame",
                    "cost": "200.00"
                },
            ]
        )

        self.assertEqual(response.status_code, 200)


    def test_procedure_detail(self):
        response = self.client.get("/procedures/1/")
        
        self.assertDictEqual(response.json(),
            {
            "id": 1,
            "description": "Consulta",
            "cost": "100.00"
            }
        )

        self.assertEqual(response.status_code, 200)


    def test_procedure_create(self):
        payload = {
            "id": 3,
            "description": "Cirurgia",
            "cost": "500.00"
        }

        response = self.client.post("/procedures/", payload)

        self.assertDictEqual(response.json(),
            {
                "id": 3,
                "description": "Cirurgia",
                "cost": "500.00"
            }
        )

        self.assertEqual(response.status_code, 201)


    def test_procedure_delete(self):
        
        response = self.client.delete("/procedures/1/")

        self.assertEqual(response.status_code, 204)


class AppointmentTestCase(APITransactionTestCase):

    def setUp(self):

        patient_one = Patient.objects.create(
            name="Vinicius Chan",
            birthdate="1995-12-09",
            sex="M",
            phone="16998882809",
            email="test2@email.com"
        )

        patient_two = Patient.objects.create(
            name="Jane Doe",
            birthdate="1995-12-07",
            sex="F",
            phone="169988782809",
            email="test3@email.com"
        )

        procedure_one = Procedure.objects.create(
            description="Exame 3",
            cost="100.00"
        )

        procedure_two = Procedure.objects.create(
            description="Exame 4",
            cost="200.00"
        )

        Appointment.objects.create(
            id=1,
            patient=patient_one,
            procedure=procedure_one,
            date="2020-10-10",
            start_at="15:00",
            end_at="18:00"
        )
    
        Appointment.objects.create(
            id=2,
            patient=patient_two,
            procedure=procedure_two,
            date="2021-10-10",
            start_at="10:00",
            end_at="12:00"
        )

    def test_appointments_list(self):

        response = self.client.get("/appointments/")

        self.assertEqual(response.json(),
            [
                {
                    "id": 1,
                    "patient": "http://testserver/patients/1/",
                    "procedure": "http://testserver/procedures/1/",
                    "date": "2020-10-10",
                    "start_at": "15:00:00",
                    "end_at": "18:00:00"
                },
                {
                    "id": 2,
                    "patient": "http://testserver/patients/2/",
                    "procedure": "http://testserver/procedures/2/",
                    "date": "2021-10-10",
                    "start_at": "10:00:00",
                    "end_at": "12:00:00"
                }
            ]
        )

        self.assertEqual(response.status_code, 200)