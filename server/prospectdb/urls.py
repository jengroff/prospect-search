from django.urls import path

from .views import ProspectView, TeamView, StudyView, ConversationMessageView


urlpatterns = [
    path('prospects/', ProspectView.as_view()),
    path('teams/', TeamView.as_view()),
    path('studies/', StudyView.as_view()),
    path('messages/', ConversationMessageView.as_view()),
]
