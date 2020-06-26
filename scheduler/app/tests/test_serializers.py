from datetime import date, time, timedelta
from decimal import Decimal

from rest_framework import serializers
from rest_framework.test import APITransactionTestCase

from app.models import Patient, Procedure, Appointment
from app.serializers import PatientSerializer, ProcedureSerializer, AppointmentSerializer
from .factories import PatientFactory, ProcedureFactory


class PatientSerializerTestCase(APITransactionTestCase):

    def setUp(self):
        self.data = {
            'name': 'Vinicius Test',
            'birthdate': '1990-09-07',
            'sex': Patient.MALE,
            'phone': '16998882809',
            'email': 'test@email.com'
        }

    def test_valid_patient_name(self):
        serializer = PatientSerializer(data=self.data)
        self.assertTrue(serializer.is_valid())

    def test_invalid_patient_name(self):
        payload = self.data
        payload.update({'name': 'V'})

        serializer = PatientSerializer(data=payload)
        self.assertFalse(serializer.is_valid())

    def test_valid_patient_phone(self):
        payload = self.data
        payload.update({'phone': '16981211201'})

        serializer = PatientSerializer(data=payload)
        serializer.is_valid(raise_exception=True)
        self.assertTrue(serializer.is_valid())

    def test_invalid_patient_phone_lower_than_9_digits(self):
        payload = self.data
        payload.update({'phone': '16981211'})

        serializer = PatientSerializer(data=payload)
        self.assertFalse(serializer.is_valid())

    def test_invalid_patient_phone_greater_than_12_digits(self):
        payload = self.data
        payload.update({'phone': '1698121120100'})

        serializer = PatientSerializer(data=payload)
        self.assertFalse(serializer.is_valid())


class ProcedureSerializerTestCase(APITransactionTestCase):

    def setUp(self):
        self.data = {
            'description': 'Exam',
            'cost': Decimal(100)
        }

    def test_valid_procedure_cost(self):
        serializer = ProcedureSerializer(data=self.data)
        self.assertTrue(serializer.is_valid())

    def test_invalid_procedure_cost(self):
        payload = self.data
        payload.update({'cost': Decimal(-500)})

        serializer = ProcedureSerializer(data=payload)
        self.assertFalse(serializer.is_valid())


class AppointmentSerializerTestCase(APITransactionTestCase):

    def setUp(self):
        patient = PatientFactory.create()
        procedure = ProcedureFactory.create()
        self.data = {
            'patient': patient.pk,
            'procedure': procedure.pk,
            'date': date.today() + timedelta(days=1),
            'start_at': time(10, 0),
            'end_at': time(12, 0)
        }

    def test_valid_appointment_date(self):
        serializer = AppointmentSerializer(data=self.data)
        self.assertTrue(serializer.is_valid())

    def test_invalid_appointment_date_lower_than_today(self):
        yesterday = date.today() - timedelta(days=1)

        payload = self.data
        payload.update({'date': yesterday})

        serializer = AppointmentSerializer(data=payload)
        self.assertFalse(serializer.is_valid())
        self.assertEqual(
            serializer.errors,
            {'date': ['Not allowed to create appointments in the past']}
        )

    def test_invalid_appointment_date_format(self):
        payload = self.data
        payload.update({'date': '12-12-12'})

        serializer = AppointmentSerializer(data=payload)
        self.assertFalse(serializer.is_valid())
        self.assertEqual(
            serializer.errors,
            {
                'date': [
                    'Date has wrong format. Use one of '
                    'these formats instead: YYYY[-MM[-DD]].'
                ]
            }
        )
