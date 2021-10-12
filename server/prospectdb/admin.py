from django.contrib import admin

from .models import Prospect, Team, Study, Question, Group, Participant, ConversationStream, ConversationMessage


@admin.register(Prospect)
class ProspectAdmin(admin.ModelAdmin):
    fields = ('id',
              'email',
              'first_name',
              'last_name',
              'phone',
              'birthday',
              'story',
              'occupation',
              'gender',
              'ethnicity',
              'country',
              'city',
              'region',
              'created_at'
              )

    list_display = ('id',
                    'email',
                    'first_name',
                    'last_name',
                    'phone',
                    'birthday',
                    'gender',
                    'ethnicity',
                    'country',
                    'city',
                    'region',
                    )

    list_filter = ('first_name',
                   'last_name',
                   'phone',
                   'birthday',
                   'gender',
                   'ethnicity',
                   'country',
                   'city')

    ordering = ('last_name',)
    readonly_fields = ('id', 'created_at')


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    fields = ('id', 'name', 'created_at')
    list_display = ('id', 'name')
    list_filter = 'name',
    ordering = ('name',)
    readonly_fields = ('id', 'created_at')


@admin.register(Study)
class StudyAdmin(admin.ModelAdmin):
    fields = ('id', 'name', 'objective', 'start_date', 'created_at', 'team_id')
    list_display = ('id', 'name', 'objective', 'team_id')
    list_filter = ('name', 'team_id')
    ordering = ('name',)
    readonly_fields = ('id', 'created_at')


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    fields = ('id', 'body', 'created_at')
    list_display = ('id', 'body')
    list_filter = ('body',)
    ordering = ('id',)
    readonly_fields = ('id', 'created_at')


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    fields = ('id', 'name', 'created_at', 'study_instructions', 'study_id')
    list_display = ('id', 'name', 'study_id')
    list_filter = ('name', 'study_id')
    ordering = ('study_id',)
    readonly_fields = ('id', 'created_at')


@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    fields = ('id', 'created_at', 'group_id', 'prospect_id')
    list_display = ('id', 'group_id', 'prospect_id')
    list_filter = ('group_id', 'prospect_id')
    ordering = ('prospect_id',)
    readonly_fields = ('id', 'created_at')


@admin.register(ConversationStream)
class ConversationStreamAdmin(admin.ModelAdmin):
    fields = ('id', 'created_at', 'participant_id', 'question_id')
    list_display = ('id', 'participant_id', 'question_id')
    list_filter = ('participant_id', 'question_id')
    readonly_fields = ('id', 'created_at')


@admin.register(ConversationMessage)
class ConversationMessageAdmin(admin.ModelAdmin):
    fields = ('id', 'text', 'created_at', 'conversation_stream_id')
    list_display = ('id', 'text', 'conversation_stream_id')
    list_filter = ('text', 'conversation_stream_id')
    ordering = ('id',)
    readonly_fields = ('id', 'created_at')
