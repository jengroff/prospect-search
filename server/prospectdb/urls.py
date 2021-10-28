from django.urls import path

from .views import ProspectView, TeamView, StudyView, ConversationMessageView, ESMessagesView


urlpatterns = [
    path('prospects/', ProspectView.as_view()),
    path('teams/', TeamView.as_view()),
    path('studies/', StudyView.as_view()),
    path('messages/', ESMessagesView.as_view()),
    path('es-messages', ESMessagesView.as_view()),
    path('pg-messages/', ConversationMessageView.as_view())
]
