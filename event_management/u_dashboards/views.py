from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from users.models import *
from events.models import Event
from django.db.models import Count, Sum

@login_required
def organizer_dashboard(request):
    if request.method == "GET":
        events = Event.objects.filter(organizer__user=request.user)
        events_count = events.count()

        active_events = events.filter(is_completed=False)
        active_events_count = active_events.count()

        actv_participants = (
        events.annotate(participant_count=Count('participants'))
          .aggregate(total_participants=Sum('participant_count'))['total_participants'] or 0
        )

        return render(request, "dashboards/organizer.html", 
                      {"user": request.user,
                       "events":events,
                       "active_events_count":active_events_count,
                       "events_count":events_count,
                       "actv_participants":actv_participants}
                      )

@login_required
def participant_dashboard(request):
    return render(request, "dashboards/participant.html", {"user": request.user})

@login_required
def volunteer_dashboard(request):
    return render(request, "dashboards/volunteer.html", {"user": request.user})
