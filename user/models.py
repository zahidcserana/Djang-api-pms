from django.db import models
from enum import Enum


class User(models.Model):
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
    ADMIN = 'ADMIN'
    USER = 'USER'
    Type = [
        (ADMIN, 'Admin'),
        (USER, 'User'),
    ]
    type = models.CharField(
        max_length=10,
        choices=Type,
        default=USER,
    )
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    mobile = models.CharField(max_length=255)

    def is_upperclass(self):
        return self.status in {self.ACTIVE, self.INACTIVE}

    def __str__(self):
        return self.name
