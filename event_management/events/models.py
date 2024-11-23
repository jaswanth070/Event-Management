from django.db import models
# from users.models import Organizer

class Event(models.Model):
    LOCATION_CHOICE = [
        ("Location1", "Location1"),
        ("Location2", "Location2"),
        ("Location3", "Location3"),
        ("Location4", "Location4"),
        ("Location5", "Location5"),
    ]
    CATEGORY_CHOICE = [
        ("WorkShop", "WorkShop"),
        ("Competition", "Competition"),
        ("Tech Talk", "Tech Talk"),
        ("Gaming", "Gaming"),
        ("Entertainment", "Entertainment"),
    ]
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True,null=True)
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=50,choices=LOCATION_CHOICE,blank=True,null=True)
    category = models.CharField(max_length=50,choices=CATEGORY_CHOICE)
    fee = models.IntegerField(default="0")
    capacity = models.IntegerField(default=0)
    organizer = models.ForeignKey("users.Organizer",on_delete=models.CASCADE,null=False,blank=False)
    participants = models.ManyToManyField("users.Participant",related_name='events_participated', blank=True)

    image = models.ImageField(upload_to="event_images/",blank=True,null=True)

    is_completed = models.BooleanField(default=False)
    accept_registrations = models.BooleanField(default=True)