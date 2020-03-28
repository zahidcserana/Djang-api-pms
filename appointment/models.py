from django.db import models
from enum import Enum
from patient.models import Patient
from doctor.models import Doctor


class AppointmentSerial(models.Model):
    ACTIVE = 'ACTIVE'
    CANCEL = 'CANCEL'
    ATTEND = 'ATTEND'
    Status = [
        (ACTIVE, 'Active'),
        (CANCEL, 'Cancel'),
        (ATTEND, 'Attend'),
    ]
    status = models.CharField(
        max_length=10,
        choices=Status,
        default=ACTIVE,
    )
    name = models.CharField(max_length=255)
    mobile = models.CharField(max_length=255)
    schedule_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    doctor = models.ForeignKey(
        'doctor.Doctor',
        null=True,
        on_delete=models.CASCADE
    )

    def is_upperclass(self):
        return self.status in {self.ACTIVE, self.INACTIVE}

    def __str__(self):
        return self.name


class DoctorAppointment(models.Model):
    name = models.CharField(max_length=255, null=True)
    mobile = models.CharField(max_length=255, null=True)
    doc_image = models.FileField()
    doc_file = models.FileField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    patient = models.ForeignKey(
        'patient.Patient',
        on_delete=models.CASCADE
    )
    doctor = models.ForeignKey(
        'doctor.Doctor',
        null=True,
        on_delete=models.CASCADE
    )
    def __str__(self):
        return self.name
