from django.db import models
from enum import Enum

from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=20, blank=True)
    department = models.CharField(max_length=100, null=True)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
        return instance.id

# class User(models.Model):
#     ACTIVE = 'ACTIVE'
#     INACTIVE = 'INACTIVE'
#     DELETE = 'DELETE'
#     Status = [
#         (ACTIVE, 'Active'),
#         (INACTIVE, 'Inactive'),
#         (DELETE, 'Delete'),
#     ]
#     status = models.CharField(
#         max_length=10,
#         choices=Status,
#         default=ACTIVE,
#     )
#     ADMIN = 'ADMIN'
#     USER = 'USER'
#     Type = [
#         (ADMIN, 'Admin'),
#         (USER, 'User'),
#     ]
#     type = models.CharField(
#         max_length=10,
#         choices=Type,
#         default=USER,
#     )
#     name = models.CharField(max_length=255)
#     email = models.CharField(max_length=255)
#     mobile = models.CharField(max_length=255)
#     company = models.IntegerField(default=1)
#     timestamp = models.DateTimeField(auto_now=True)
#     department = models.ForeignKey(
#         'setting.Department',
#         related_name='departments',
#         on_delete=models.CASCADE
#     )
#
#     def is_upperclass(self):
#         return self.status in {self.ACTIVE, self.INACTIVE}
#
#     def __str__(self):
#         return self.name
