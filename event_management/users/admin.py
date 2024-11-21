from django.contrib import admin

from .models import *

admin.site.register(UserProfile)
admin.site.register(Organizer)
admin.site.register(Participant)
admin.site.register(Volunteer)
