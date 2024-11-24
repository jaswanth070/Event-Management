
from django.contrib import admin
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path("organizer/events/create/", create_event, name="create_event"),
    path("organizer/myevents/", myevents, name="my_events"),
    path("organizer/myevents/<str:event_id>", editEvent, name="event"),
    path("organizer/myevents/<str:event_id>/delete", deleteEvent, name="deleteEvent"),
    path("organizer/account",editAccount,name="editAccoutn"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
