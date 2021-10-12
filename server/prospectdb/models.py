import uuid
from datetime import datetime
from django.db import models


class Prospect(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )
    email = models.CharField(max_length=255)
    first_name = models.CharField(max_length=64, null=True)
    last_name = models.CharField(max_length=64, null=True)
    phone = models.CharField(max_length=64, null=True)
    birthday = models.DateTimeField(null=True)
    gender = models.CharField(max_length=64, null=True)
    story = models.TextField(null=True)
    occupation = models.CharField(max_length=128, null=True)
    country = models.CharField(max_length=255, null=True)
    region = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=255, null=True)
    ethnicity = models.CharField(max_length=255, null=True)
    registered_at = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.id}'