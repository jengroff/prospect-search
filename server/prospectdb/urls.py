from django.urls import path

from .views import ProspectView


urlpatterns = [
    path('prospects/', ProspectView.as_view()),
]