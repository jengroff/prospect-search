from django.contrib import admin

from .models import Prospect, Team, Study, Question, Participant, Group, ConversationStream, ConversationMessage, ConversationMessageWord


@admin.register(Prospect)
class ProspectAdmin(admin.ModelAdmin):
    fields = ('id',
              'email',
              'first_name',
              'last_name',
              'phone',
              'story',
              'occupation',
              'gender',
              'ethnicity',
              'country',
              'city',
              'region',
              )

    list_display = ('id',
                    'email',
                    'first_name',
                    'last_name',
                    'phone',
                    'gender',
                    'ethnicity',
                    'country',
                    'city',
                    'region',
                    )

    list_filter = ('first_name',
                   'last_name',
                   'phone',
                   'gender',
                   'ethnicity',
                   'country',
                   'city')

    ordering = ('first_name',)
    readonly_fields = ('id',)


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    fields = ('id', 'name')
    list_display = ('id', 'name')
    list_filter = 'name',
    ordering = ('name',)
    readonly_fields = ('id',)


@admin.register(Study)
class StudyAdmin(admin.ModelAdmin):
    fields = ('id', 'name', 'objective', 'team_id')
    list_display = ('id', 'name', 'objective', 'team_id')
    list_filter = ('name', 'team_id')
    ordering = ('name',)
    readonly_fields = ('id',)


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    fields = ('id', 'body')
    list_display = ('id', 'body')
    list_filter = ('body',)
    ordering = ('id',)
    readonly_fields = ('id',)


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    fields = ('id', 'name', 'study_id')
    list_display = ('id', 'name', 'study_id')
    list_filter = ('name', 'study_id')
    ordering = ('study_id',)
    readonly_fields = ('id',)


@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    fields = ('id', 'prospect_id', 'group_id')
    list_display = ('id', 'prospect_id', 'group_id')
    list_filter = ('prospect_id',)
    ordering = ('prospect_id',)
    readonly_fields = ('id',)


@admin.register(ConversationStream)
class ConversationStreamAdmin(admin.ModelAdmin):
    fields = ('id', 'participant_id', 'question_id')
    list_display = ('id', 'participant_id', 'question_id')
    list_filter = ('participant_id', 'question_id')
    readonly_fields = ('id',)


@admin.register(ConversationMessage)
class ConversationMessageAdmin(admin.ModelAdmin):
    fields = ('id', 'text', 'conversation_stream_id', 'search_vector')
    list_display = ('id', 'text', 'conversation_stream_id')
    list_filter = ('text', 'conversation_stream_id')
    ordering = ('id',)
    readonly_fields = ('id',)


@admin.register(ConversationMessageWord)
class ConversationMessageWordAdmin(admin.ModelAdmin):
    fields = ('word',)
    list_display = ('word',)
    ordering = ('word',)
