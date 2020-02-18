from django.db import models


class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    mobile = models.CharField(max_length=255)

    def __str__(self):
        return self.name
