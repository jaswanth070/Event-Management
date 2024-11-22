from django.db import models
# from users.models import Organizer

class Event(models.Model):
    id = models.CharField(max_length=10,primary_key=True,null=False,unique=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True,null=True)
    date = models.DateField()
    time = models.TimeField()
    organizer = models.ForeignKey("users.Organizer",on_delete=models.CASCADE,null=False,blank=False)
    participants = models.ManyToManyField("users.Participant",related_name='events_participated', blank=True)

    is_completed = models.BooleanField(default=False)
    accept_registrations = models.BooleanField(default=True)