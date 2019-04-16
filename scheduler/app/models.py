# -*- coding: utf-8 -*-

from django.db import models

class Patient(models.Model):
    """ Representative class for patients. """
    
    MALE, FEMALE = 'male', 'female'

    SEX_CHOICES = (
        (MALE, 'male'),
        (FEMALE, 'female')
    )

    name = models.CharField(max_length=60, verbose_name='Name')
    birthdate = models.DateField(max_length=3, verbose_name='Birth Date')
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, verbose_name='Sex')
    phone = models.CharField(max_length=20, verbose_name='Phone')
    email = models.EmailField(verbose_name='E-mail')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Paciente'

class Procedure(models.Model):
    """ Representative class for the procedures """

    description = models.CharField(max_length=100, verbose_name='Procedimento')
    cost = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Valor')

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Procedimento'

class Appointment(models.Model):
    """ Representative class for the appointments """

    patient = models.ForeignKey("Patient", related_name="patient")
    procedure = models.ForeignKey("Procedure", related_name="procedure")
    date = models.DateField()
    start_at = models.TimeField(null=False)
    end_at = models.TimeField()

    def __str__(self):
        return "{} - {}, dia {} às {} horas".format(self.patient.name, self.procedure.description, self.date, self.start_at)
    
    class Meta:
        verbose_name = 'Agendamento'