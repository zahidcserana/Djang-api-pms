from django.db import models
from enum import Enum


class Doctor(models.Model):
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
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    education = models.CharField(max_length=255)
    experience = models.CharField(max_length=255)
    organisation = models.CharField(max_length=255, null=True)
    location = models.CharField(max_length=255, null=True)
    mobile = models.CharField(max_length=255)
    address = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def is_upperclass(self):
        return self.status in {self.ACTIVE, self.INACTIVE}

    def __str__(self):
        return self.name


