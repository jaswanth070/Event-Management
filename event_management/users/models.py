from django.db import models
from django.contrib.auth.models import User,AbstractUser
from events.models import Event

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



class Organizer(models.Model):
    user = models.OneToOneField(UserProfile,on_delete=models.CASCADE,related_name="Organizer_Profile")
    events_managed = models.PositiveIntegerField(default=0)
    # def __str__(self):
    #     return f"{self.user.username}"

class Participant(models.Model):
    user = models.OneToOneField(UserProfile,on_delete=models.CASCADE,related_name="Participant_Profile")
    registered_events = models.ManyToManyField("events.Event",related_name='participants_in_event',blank=True)

class Volunteer(models.Model):
    user = models.OneToOneField(UserProfile,on_delete=models.CASCADE,related_name="Volunteer_Profile")
    assigned_events = models.ManyToManyField("events.Event",blank=True)
