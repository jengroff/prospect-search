# Generated by Django 3.1.7 on 2021-10-22 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prospectdb', '0005_update_search_vector'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConversationMessageWord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.TextField(unique=True)),
            ],
        ),
    ]
