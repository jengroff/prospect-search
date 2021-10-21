import uuid
from django.db import models


class Team(models.Model):
    id = models.IntegerField(primary_key=True, editable=False, auto_created=True)
    name = models.CharField(max_length=128, null=True)

    def __str__(self):
        return f'{self.name}'


class Prospect(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.CharField(max_length=255)
    first_name = models.CharField(max_length=64, null=True)
    last_name = models.CharField(max_length=64, null=True)
    phone = models.CharField(max_length=64, null=True)
    gender = models.CharField(max_length=64, null=True)
    story = models.TextField(null=True)
    occupation = models.CharField(max_length=128, null=True)
    country = models.CharField(max_length=255, null=True)
    region = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=255, null=True)
    ethnicity = models.CharField(max_length=255, null=True)

    def __str__(self):
        return f'{self.email}'


class Study(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True, editable=False)
    name = models.CharField(max_length=128, null=True)
    objective = models.TextField(null=True)
    team_id = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="studies", related_query_name="study")

    def __str__(self):
        return f'{self.name}'


class Question(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    body = models.TextField(null=True)

    def __str__(self):
        return f'{self.id}'


class Group(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)
    name = models.CharField(max_length=128, null=True)
    study_id = models.ForeignKey(Study,
                                 on_delete=models.CASCADE,
                                 related_name="groups",
                                 related_query_name="group"
                                 )

    def __str__(self):
        return f'{self.name}'


class Participant(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True, editable=False)
    group_id = models.ForeignKey(Group, on_delete=models.CASCADE, null=True)
    prospect_id = models.ForeignKey(Prospect, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id}'


class ConversationStream(models.Model):
    id = models.IntegerField(primary_key=True, editable=False)
    participant_id = models.ForeignKey(Participant, on_delete=models.CASCADE)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id}'


class ConversationMessage(models.Model):
    id = models.IntegerField(primary_key=True, editable=False)
    text = models.TextField(null=True)
    conversation_stream_id = models.ForeignKey(
        ConversationStream,
        on_delete=models.CASCADE,
        related_name="groups",
        related_query_name="group",
        null=True
    )

    def __str__(self):
        return f'{self.id}'
