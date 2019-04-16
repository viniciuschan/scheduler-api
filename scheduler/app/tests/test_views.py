from datetime import date
from decimal import Decimal

from rest_framework import serializers
from rest_framework.test import APITransactionTestCase

from .factories import PatientFactory, ProcedureFactory, AppointmentFactory
from app.models import Patient, Procedure, Appointment


class PatientViewSetTestCase(APITransactionTestCase):
    """ Test cases for Patient View """

    def setUp(self):
        self.patient_one = PatientFactory.create(
            name='Patient One',
            birthdate='1990-09-07',
            sex=Patient.MALE,
            phone='16998882809',
            email='test1@email.com'
        )
        self.patient_two = PatientFactory.create(
            name='Patient Two',
            birthdate='2017-12-10',
            sex=Patient.FEMALE,
            phone='16982129227',
            email='test2@email.com'
        )

    def test_create_patient(self):
        url = '/patients/'
        payload = {
            'name': 'Patient Test',
            'birthdate': date.today(),
            'sex': Patient.FEMALE,
            'phone': '16998882809',
            'email': 'test@email.com'
        }
        response = self.client.post(url, payload)

        self.assertEqual(response.status_code, 201)

    def test_create_patient_with_invalid_name(self):
        url = '/patients/'
        payload = {
            'name': 'A',
            'birthdate': date.today(),
            'sex': Patient.FEMALE,
            'phone': '16998882809',
            'email': 'test@email.com'
        }
        response = self.client.post(url, payload)

        self.assertEqual(response.status_code, 400)
        self.assertRaises(serializers.ValidationError)

    def test_create_patient_with_invalid_phone(self):
        url = '/patients/'
        payload = {
            'name': 'Patient Invalid Phone',
            'birthdate': date.today(),
            'sex': Patient.FEMALE,
            'phone': '12345678',
            'email': 'test@email.com'
        }
        response = self.client.post(url, payload)

        self.assertEqual(response.status_code, 400)
        self.assertRaises(serializers.ValidationError)

    def test_list_patient(self):
        response = self.client.get('/patients/')

        self.assertEqual(response.json().get('results'), [
            {
                'id': self.patient_one.id,
                'name': 'Patient One',
                'birthdate': '1990-09-07',
                'sex': Patient.MALE,
                'phone': '16998882809',
                'email': 'test1@email.com'
            },
            {
                'id': self.patient_two.id,
                'name': 'Patient Two',
                'birthdate': '2017-12-10',
                'sex': Patient.FEMALE,
                'phone': '16982129227',
                'email': 'test2@email.com'
            }
        ])
        self.assertEqual(Patient.objects.count(), 2)
        self.assertEqual(response.status_code, 200)

    def test_detail_patient(self):
        patient = PatientFactory.create(
            name='Patient Three',
            birthdate='1990-10-15',
            sex=Patient.MALE,
            phone='16998882809',
            email='test3@email.com'
        )
        url_detail = '/patients/{}/'.format(patient.id)
        response = self.client.get(url_detail)

        self.assertDictEqual(response.json(), {
            'id': patient.id,
            'name': 'Patient Three',
            'birthdate': '1990-10-15',
            'sex': Patient.MALE,
            'phone': '16998882809',
            'email': 'test3@email.com'
        })
        self.assertEqual(response.status_code, 200)

    def test_update_patient(self):
        patient = PatientFactory.create()
        url_update = '/patients/{}/'.format(patient.id)

        payload = {
            'name': 'Test Patient Update',
            'birthdate': date.today(),
            'sex': Patient.MALE,
            'phone': '(16)90288-2309',
            'email': 'test_patient@gmail.com'
        }
        response = self.client.put(url_update, payload)
        self.assertEqual(response.status_code, 200)

    def test_partial_update_patient(self):
        patient = PatientFactory.create()
        url_partial_update = '/patients/{}/'.format(patient.id)

        payload = {
            'name': 'Patient Four',
            'birthdate': date.today(),
            'sex': Patient.FEMALE,
            'phone': '16902882309',
            'email': 'test4@gmail.com'
        }
        response = self.client.patch(url_partial_update, payload)
        self.assertEqual(response.status_code, 200)

    def test_delete_patient(self):
        response = self.client.delete('/patients/1/')
        self.assertEqual(response.status_code, 204)

class ProcedureViewSetTestCase(APITransactionTestCase):
    """ Tese cases for Procedure Model """

    def setUp(self):
        self.procedure_one = ProcedureFactory.create(
            description='Exam',
            cost=Decimal(100)
        )
        self.procedure_two = ProcedureFactory.create(
            description='Surgery',
            cost=Decimal(500)
        )

    def test_list_procedures(self):
        response = self.client.get('/procedures/')

        self.assertEqual(response.json().get('results'), [
            {
                'id': self.procedure_one.id,
                'description': 'Exam',
                'cost': '100.00'
            },
            {
                'id': self.procedure_two.id,
                'description': 'Surgery',
                'cost': '500.00'
            }
        ])
        self.assertEqual(Procedure.objects.count(), 2)
        self.assertEqual(response.status_code, 200)

    def test_detail_procedure(self):
        url_detail = '/procedures/{}/'.format(self.procedure_one.id)
        response = self.client.get('/procedures/1/')

        self.assertDictEqual(response.json(),{
            'id': self.procedure_one.id,
            'description': 'Exam',
            'cost': '100.00'
        })
        self.assertEqual(response.status_code, 200)

    def test_create_procedure(self):
        payload = {
            'description': 'Extraction',
            'cost': Decimal(200)
        }
        response = self.client.post('/procedures/', payload, format='json')

        self.assertEqual(response.status_code, 201)

    def test_create_procedure_with_negative_price(self):
        payload = {
            'description': 'Exam with negative price',
            'cost': Decimal(-100)
        }
        response = self.client.post('/procedures/', payload, format='json')

        self.assertEqual(response.status_code, 400)
        self.assertRaises(serializers.ValidationError)

    def test_partial_update_procedure(self):
        payload = {
            'description': 'Full Exam',
            'cost': Decimal(500)
        }
        response = self.client.patch('/procedures/2/', payload)
        self.assertEqual(response.status_code, 200)

    def test_update_procedure(self):
        payload = {
            'description': 'Advanced Exam',
            'cost': Decimal(1200)
        }
        response = self.client.put('/procedures/2/', payload)
        self.assertEqual(response.status_code, 200)

    def test_delete_procedure(self):

        response = self.client.delete('/procedures/1/')
        self.assertEqual(response.status_code, 204)

class AppointmentViewSetTestCase(APITransactionTestCase):

    def setUp(self):
        self.patient_one = PatientFactory.create(
            name='Vinicius Chan',
            birthdate='1995-12-09',
            sex=Patient.MALE,
            phone='16998882809',
            email='test2@gmail.com'
        )
        self.patient_two = PatientFactory.create(
            name='Jane Doe',
            birthdate='1995-12-07',
            sex=Patient.FEMALE,
            phone='169988782809',
            email='test3@gmail.com'
        )
        self.procedure_one = ProcedureFactory.create(
            description='Exam 1',
            cost=Decimal(100)
        )
        self.procedure_two = ProcedureFactory.create(
            description='Exam 4',
            cost=Decimal(200)
        )
        self.appointment_one = AppointmentFactory.create(
            patient=self.patient_one,
            procedure=self.procedure_one,
            date='2020-10-10',
            start_at='15:00:00',
            end_at='18:00:00'
        )
        self.appointment_two = AppointmentFactory.create(
            patient=self.patient_two,
            procedure=self.procedure_two,
            date='2021-10-10',
            start_at='10:00:00',
            end_at='12:00:00'
        )

    def test_list_appointment(self):
        response = self.client.get('/appointments/')

        self.assertEqual(response.json().get('results'), [
            {
                'id': self.appointment_one.id,
                'patient': self.patient_one.id,
                'procedure': self.procedure_one.id,
                'date': '2020-10-10',
                'start_at': '15:00:00',
                'end_at': '18:00:00'
            },
            {
                'id': self.patient_two.id,
                'patient': self.patient_two.id,
                'procedure': self.procedure_two.id,
                'date': '2021-10-10',
                'start_at': '10:00:00',
                'end_at': '12:00:00'
            }
        ])
        self.assertEqual(Appointment.objects.count(), 2)
        self.assertEqual(response.status_code, 200)

    def test_detail_appointment(self):
        url_detail = '/appointments/{}/'.format(self.appointment_one.id)
        response = self.client.get(url_detail)

        self.assertDictEqual(response.json(), {
                'id': self.appointment_one.id,
                'patient': self.patient_one.id,
                'procedure': self.procedure_one.id,
                'date': '2020-10-10',
                'start_at': '15:00:00',
                'end_at': '18:00:00'
        })
        self.assertEqual(response.status_code, 200)

    def test_partial_update_appointment(self):
        payload = {
            'start_at': '11:00:00'
        }
        response = self.client.patch('/appointments/1/', payload)
        self.assertEqual(response.status_code, 200)

    def test_update_appointment(self):
        appointment = AppointmentFactory.create()
        url_update = '/appointments/{}/'.format(appointment.id)

        payload = {
            'patient': self.patient_one.id,
            'procedure': self.procedure_two.id,
            'date': '2021-10-10',
            'start_at': '10:00:00',
            'end_at': '11:30:00'
        }
        response = self.client.put(url_update, payload)
        self.assertEqual(response.status_code, 200)

    def test_create_appointment(self):
        payload = {
            'patient': self.patient_one.id,
            'procedure': self.patient_two.id,
            'date': '2021-10-10',
            'start_at': '10:00:00',
            'end_at': '12:00:00'
        }
        response = self.client.post('/appointments/', payload, format='json')
        self.assertEqual(response.status_code, 201)

    def test_create_appointment_in_the_past(self):
        payload = {
            'patient': self.patient_one.id,
            'procedure': self.patient_two.id,
            'date': '2018-10-10',
            'start_at': '10:00:00',
            'end_at': '12:00:00'
        }
        response = self.client.post('/appointments/', payload, format='json')
        self.assertEqual(response.status_code, 400)
        self.assertRaises(serializers.ValidationError)

    def test_delete_appointment(self):
        response = self.client.delete('/appointments/2/')
        self.assertEqual(response.status_code, 204)
