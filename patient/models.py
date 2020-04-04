from django.db import models
from enum import Enum


class Patient(models.Model):
    ACTIVE = 'ACTIVE'
    INACTIVE = 'INACTIVE'
    DELETE = 'DELETE'
    Status = [
        (ACTIVE, 'Active'),
        (INACTIVE, 'Inactive'),
        (DELETE, 'Delete'),
    ]
    status = models.CharField(
        max_length=10,
        choices=Status,
        default=ACTIVE,
    )
    REGULAR = 'REGULAR'
    IRREGULAR = 'IRREGULAR'
    Type = [
        (REGULAR, 'Regular'),
        (IRREGULAR, 'Irregular'),
    ]
    type = models.CharField(
        max_length=10,
        choices=Type,
        default=REGULAR,
    )
    MALE = 'MALE'
    FEMALE = 'FEMALE'
    Gender = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    ]
    gender = models.CharField(
        max_length=10,
        choices=Gender,
        default=MALE,
    )
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    mobile = models.CharField(max_length=255)
    age = models.IntegerField(null=True)
    address = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def is_upperclass(self):
        return self.status in {self.ACTIVE, self.INACTIVE}

    def __str__(self):
        return self.name


class PatientPayment(models.Model):
    description = models.CharField(max_length=255, null=True)
    amount = models.FloatField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    patient = models.ForeignKey(
        'patient.Patient',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.patient.name
