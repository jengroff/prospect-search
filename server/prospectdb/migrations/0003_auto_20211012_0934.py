# Generated by Django 3.1.7 on 2021-10-12 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prospectdb', '0002_auto_20211012_0928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='body',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='order',
            field=models.SmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='study',
            name='start_date',
            field=models.DateTimeField(null=True),
        ),
    ]