# Generated by Django 3.1.7 on 2021-10-12 09:22

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.IntegerField(auto_created=True, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('study_instructions', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.IntegerField(auto_created=True, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Study',
            fields=[
                ('id', models.IntegerField(auto_created=True, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128, null=True)),
                ('objective', models.TextField(null=True)),
                ('start_date', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('team_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='studies', related_query_name='study', to='prospectdb.team')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255, null=True)),
                ('body', models.TextField()),
                ('order', models.SmallIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('study_instructions', models.TextField(null=True)),
                ('study_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', related_query_name='question', to='prospectdb.study')),
            ],
        ),
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
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('team_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prospects', related_query_name='prospect', to='prospectdb.team')),
            ],
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.IntegerField(auto_created=True, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('group_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prospectdb.group')),
                ('prospect_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prospectdb.prospect')),
            ],
        ),
        migrations.AddField(
            model_name='group',
            name='study_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='groups', related_query_name='group', to='prospectdb.study'),
        ),
        migrations.CreateModel(
            name='ConversationStream',
            fields=[
                ('id', models.IntegerField(editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('participant_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prospectdb.participant')),
                ('question_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prospectdb.question')),
            ],
        ),
        migrations.CreateModel(
            name='ConversationMessage',
            fields=[
                ('id', models.IntegerField(editable=False, primary_key=True, serialize=False)),
                ('text', models.TextField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('conversation_stream_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='groups', related_query_name='group', to='prospectdb.conversationstream')),
            ],
        ),
    ]
