from django.contrib import admin
from django.contrib.auth.models import User

from .models import *


admin.site.register(UserProfile)
admin.site.register(Organizer)
admin.site.register(Participant)
admin.site.register(Volunteer)
