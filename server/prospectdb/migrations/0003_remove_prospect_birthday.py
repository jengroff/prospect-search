# Generated by Django 3.1.7 on 2021-10-21 02:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prospectdb', '0002_remove_study_start_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prospect',
            name='birthday',
        ),
    ]
