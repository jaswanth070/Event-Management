from django.urls import path
from .views import *

urlpatterns = [
    path('organizer', organizer_dashboard, name='organizer_dashboard'),
    path('participant', participant_dashboard, name='participant_dashboard'),
    path('volunteer', volunteer_dashboard, name='volunteer_dashboard'),
]
