# Generated by Django 3.1.7 on 2021-10-12 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prospectdb', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prospect',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
