# Generated by Django 3.1.7 on 2021-10-12 10:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prospectdb', '0004_auto_20211012_0953'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prospect',
            name='registered_at',
        ),
        migrations.RemoveField(
            model_name='prospect',
            name='team_id',
        ),
    ]