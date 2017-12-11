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


    def test_patient_update(self):

        payload = {        
            "id": 1,
            "name": "Teste Paciente 7",
            "birthdate": "2010-12-09",
            "sex": "F",
            "phone": "16902882309",
            "email": "testepaciente7@gmail.com"
        }

        response = self.client.put("/patients/2/", payload)
        self.assertEqual(response.status_code, 200)

    def test_patient_partial_update(self):

        payload = {        
            "id": 1,
            "name": "Teste Paciente 25",
            "birthdate": "2010-12-09",
            "sex": "F",
            "phone": "16902882309",
            "email": "testepaciente7@gmail.com"
        }

        response = self.client.patch("/patients/2/", payload)
        self.assertEqual(response.status_code, 200)


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
                }
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
            "description": "coleta exame",
            "cost": "100.00"
        }

        response = self.client.post("/procedures/", payload)
        self.assertEqual(response.status_code, 201)


    def test_procedure_partial_update(self):

        payload = {
            "description": "Consulta",
            "cost": "500.00"
        }

        response = self.client.patch("/procedures/2/", payload)
        self.assertEqual(response.status_code, 200)


    def test_procedure_update(self):
        payload = {
            "description": "Tratamento avançado",
            "cost": "1200.00"
        }

        response = self.client.put("/procedures/2/", payload)
        self.assertEqual(response.status_code, 200)


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
            email="test2@gmail.com"
        )

        patient_two = Patient.objects.create(
            name="Jane Doe",
            birthdate="1995-12-07",
            sex="F",
            phone="169988782809",
            email="test3@gmail.com"
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
            start_at="15:00:00",
            end_at="18:00:00"
        )
    
        Appointment.objects.create(
            id=2,
            patient=patient_two,
            procedure=procedure_two,
            date="2021-10-10",
            start_at="10:00:00",
            end_at="12:00:00"
        )


    def test_appointment_list(self):

        response = self.client.get("/appointments/")

        self.assertEqual(response.json(),
            [
                {
                    "id": 1,
                    "patient": "http://testserver/patients/3/",
                    "procedure": "http://testserver/procedures/3/",
                    "date": "2020-10-10",
                    "start_at": "15:00:00",
                    "end_at": "18:00:00"
                },
                {
                    "id": 2,
                    "patient": "http://testserver/patients/4/",
                    "procedure": "http://testserver/procedures/4/",
                    "date": "2021-10-10",
                    "start_at": "10:00:00",
                    "end_at": "12:00:00"
                }
            ]
        )

        self.assertEqual(response.status_code, 200)

    def test_appointment_detail(self):

        response = self.client.get("/appointments/2/")

        self.assertDictEqual(response.json(),
            {
                "id": 2,
                "patient": "http://testserver/patients/4/",
                "procedure": "http://testserver/procedures/4/",
                "date": "2021-10-10",
                "start_at": "10:00:00",
                "end_at": "12:00:00"
            }
        )
        self.assertEqual(response.status_code, 200)

    
    def test_appointment_partial_update(self):

        payload = {
            "start_at": "11:00:00"
        }

        response = self.client.patch("/appointments/1/", payload)
        self.assertEqual(response.status_code, 200)


    def test_appointment_update(self):
        
        payload = {
            "patient": "https://testserver/patients/4/",
            "procedure": "http://testserver/procedures/4/",
            "date": "2016-09-11",
            "start_at": "07:00:00",
            "end_at": "19:00:00"
        }

        response = self.client.put("/appointments/1/", payload)
        self.assertEqual(response.status_code, 200)


    def test_appointment_delete(self):
        
        response = self.client.delete("/appointments/2/")
        self.assertEqual(response.status_code, 204)



