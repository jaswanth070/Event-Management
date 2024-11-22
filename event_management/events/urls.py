
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    # path('getEventDetails/<str:event_id>/', getEventDetails, name='getEventDetails'),
    path('event/<str:event_id>/', EventDetailsView.as_view(), name='event_details'),
]
