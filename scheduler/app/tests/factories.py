from decimal import Decimal
from datetime import date, time, timedelta

from factory import SubFactory
from factory.django import DjangoModelFactory

from app.models import Patient, Procedure, Appointment


class PatientFactory(DjangoModelFactory):
    """ Factory that represents a Patient model object """

    class Meta:
        model = Patient

    name = 'Testing'
    birthdate = date.today() - timedelta(days=30*12*25)
    sex = Patient.MALE
    phone = '(16)98121-1201'
    email = 'testing@email.com'


class ProcedureFactory(DjangoModelFactory):
    """ Factory that represents a Procedure model object """

    class Meta:
        model = Procedure

    description = 'Procedure Test'
    cost = Decimal(100)


class AppointmentFactory(DjangoModelFactory):
    """ Factory that represents an Appointment model object """

    class Meta:
        model = Appointment

    patient = SubFactory(PatientFactory)
    procedure = SubFactory(ProcedureFactory)
    date = date.today()
    start_at = time(15, 0)
    end_at = time(16, 0)
