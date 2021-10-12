# Generated by Django 3.1.7 on 2021-10-12 01:31

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prospect',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=255)),
                ('first_name', models.CharField(max_length=64, null=True)),
                ('last_name', models.CharField(max_length=64, null=True)),
                ('phone', models.CharField(max_length=64, null=True)),
                ('birthday', models.DateTimeField(null=True)),
                ('gender', models.CharField(max_length=64, null=True)),
                ('story', models.TextField(null=True)),
                ('occupation', models.CharField(max_length=128, null=True)),
                ('country', models.CharField(max_length=255, null=True)),
                ('region', models.CharField(max_length=255, null=True)),
                ('city', models.CharField(max_length=255, null=True)),
                ('ethnicity', models.CharField(max_length=255, null=True)),
                ('registered_at', models.DateTimeField(null=True)),
                ('created_at', models.DateTimeField(null=True)),
            ],
        ),
    ]
