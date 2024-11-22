from django.urls import path
from .views import *

urlpatterns = [
    path('register/', register, name='register'),
     path('login/', login_view, name='login'),
     path('logout/', logout_view, name='logout'),
    # path('register/role/', views.role_selection, name='role_selection'),
    # path('register/organizer/', views.organizer_register, name='organizer_register'),
    # path('register/participant/', views.participant_register, name='participant_register'),
    # path('register/volunteer/', views.volunteer_register, name='volunteer_register'),
]
