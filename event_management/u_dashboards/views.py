from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def organizer_dashboard(request):
    return render(request, "dashboards/organizer.html", {"user": request.user})

@login_required
def participant_dashboard(request):
    return render(request, "dashboards/participant.html", {"user": request.user})

@login_required
def volunteer_dashboard(request):
    return render(request, "dashboards/volunteer.html", {"user": request.user})
