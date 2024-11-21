from django.db import models
from django.contrib.auth.models import User,AbstractUser

class UserProfile(AbstractUser):
    ROLES_CHOICE = [
        ('organizer','Organizer'),
        ('participant','Participant'),
        ('volunteer','Volunteer'),
    ]

    role = models.CharField(max_length=15,choices=ROLES_CHOICE)
    phone_number = models.CharField(max_length=12,blank=True,null=True)
    institute = models.CharField(max_length=10,blank=True,null=True)

    groups = models.ManyToManyField('auth.Group',related_name="userprofile_groups",blank=True)
    user_permissions = models.ManyToManyField('auth.Permission',related_name="userprofile_permissions",blank=True)
    class Meta:
        verbose_name = "UserProfile"

class Event(models.Model):
    id = models.CharField(max_length=10,primary_key=True,null=False,unique=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True,null=True)
    date = models.DateField()
    time = models.TimeField()

class Organizer(models.Model):
    user = models.OneToOneField(UserProfile,on_delete=models.CASCADE,related_name="Organizer_Profile")
    events_managed = models.PositiveIntegerField(default=0)

class Participant(models.Model):
    user = models.OneToOneField(UserProfile,on_delete=models.CASCADE,related_name="Participant_Profile")
    registered_events = models.ManyToManyField('Event',blank=True)

class Volunteer(models.Model):
    user = models.OneToOneField(UserProfile,on_delete=models.CASCADE,related_name="Volunteer_Profile")
    assigned_events = models.ManyToManyField(Event,blank=True)
