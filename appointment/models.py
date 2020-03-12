from django.db import models
from enum import Enum
from patient.models import Patient


class AppointmentSerial(models.Model):
    ACTIVE = 'ACTIVE'
    HOLD = 'HOLD'
    CANCEL = 'CANCEL'
    REJECT = 'REJECT'
    COMPLETE = 'COMPLETE'
    DELETE = 'DELETE'
    Status = [
        (ACTIVE, 'Active'),
        (HOLD, 'Hold'),
        (CANCEL, 'Cancel'),
        (REJECT, 'Reject'),
        (COMPLETE, 'Complete'),
        (DELETE, 'Delete'),
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

    def is_upperclass(self):
        return self.status in {self.ACTIVE, self.INACTIVE}

    def __str__(self):
        return self.name


class DoctorAppointment(models.Model):
    doc_image = models.TextField()
    doc_file = models.TextField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    patient = models.ForeignKey(
        'patient.Patient',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name
