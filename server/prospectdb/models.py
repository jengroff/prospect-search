import uuid

from django.db import models


class Prospect(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255, null=True)
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=255, null=True)
    birthday = models.CharField(max_length=255, null=True)
    gender = models.CharField(max_length=255, null=True)
    bio = models.TextField(null=True, blank=True)
    ethnicity = models.CharField(max_length=255, null=True)
    country = models.CharField(max_length=255, null=True)
    region = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=255, null=True)

    def __str__(self):
        return f'{self.id}'