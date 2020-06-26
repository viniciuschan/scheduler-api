from decimal import Decimal

from rest_framework.test import APITransactionTestCase

from app.models import Patient, Procedure, Appointment
from .factories import PatientFactory, ProcedureFactory


class PatientModelTestCase(APITransactionTestCase):

    def setUp(self):
        self.patient = Patient.objects.create(
            name='Patient Test',
            birthdate='1990-09-07',
            sex=Patient.MALE,
            phone='16998882809',
            email='patient_test@email.com'
        )

    def test_patient_str(self):
        patient_str = '<{} ID: {}> Name: {}'.format(
            'Patient',
            self.patient.pk,
            self.patient.name
        )
        self.assertEqual(str(self.patient), patient_str)

    def test_instance(self):
        self.assertIsInstance(self.patient, Patient)


class ProcedureModelTestCase(APITransactionTestCase):

    def setUp(self):
        self.procedure = Procedure.objects.create(
            description='Exam',
            cost=Decimal(100)
        )

    def test_procedure_str(self):
        procedure_str = '<{} ID: {}> Description: {}'.format(
            'Procedure',
            self.procedure.pk,
            self.procedure.description
        )
        self.assertEqual(str(self.procedure), procedure_str)

    def test_procedure_instance(self):
        self.assertIsInstance(self.procedure, Procedure)


class AppointmentModelTestCase(APITransactionTestCase):

    def setUp(self):
        self.patient = PatientFactory.create()
        self.procedure = ProcedureFactory.create()
        self.appointment = Appointment.objects.create(
            patient=self.patient,
            procedure=self.procedure,
            date='2020-10-10',
            start_at='15:00:00',
            end_at='18:00:00'
        )

    def test_appointment_str(self):
        appointment_str = '<{} ID: {}> Scheduled on {} - {} hours'.format(
            'Appointment',
            self.appointment.pk,
            self.appointment.date,
            self.appointment.start_at
        )
        self.assertEqual(str(self.appointment), appointment_str)

    def test_appointment_instance(self):
        self.assertIsInstance(self.appointment, Appointment)
