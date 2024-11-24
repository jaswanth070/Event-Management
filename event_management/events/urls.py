
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path("organizer/event/<str:event_id>/", EventDetailsView.as_view(),name="event"),
    path("organizer/events/create/", create_event, name="create_event"),
    # path("organizer/create_event", ,name="create_event")
]
