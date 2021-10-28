from django.urls import path

from .views import (
    ProspectView,
    ProspectSearchWordsView,
    ESProspectsView,
    ESProspectSearchWordsView,
    ConversationMessageView,
    ESMessagesView,
    TeamView,
    StudyView,
)

urlpatterns = [
    path('prospects/', ESProspectsView.as_view()),
    path('es-prospects/', ESProspectsView.as_view()),
    path('pg-prospects', ProspectView.as_view()),
    path('prospect-search-words/', ESProspectSearchWordsView.as_view()),
    path('es-prospect-search-words/', ESProspectSearchWordsView.as_view()),
    path('pg-prospect-search-words/', ProspectSearchWordsView.as_view()),
    path('teams/', TeamView.as_view()),
    path('studies/', StudyView.as_view()),
    path('messages/', ESMessagesView.as_view()),
    path('es-messages', ESMessagesView.as_view()),
    path('pg-messages/', ConversationMessageView.as_view()),
]
