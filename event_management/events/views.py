from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from events.models import Event
from django.utils.decorators import method_decorator
from django.views import View
from django.http import JsonResponse
from .models import *
import json

def getEventDetails(request, event_id):
    event = get_object_or_404(Event,id=event_id)
    event_details = {
        "id":event.id,
        "name": event.name,
        "description": event.description,
        "date": event.date,
        "time": event.time,
        "is_completed": event.is_completed,
        "accept_registrations": event.accept_registrations,
        "organizer": event.organizer.user.first_name, 
    }
    return JsonResponse(event_details)

@method_decorator(csrf_exempt, name='dispatch')
class EventDetailsView(View):
    def get(self, request, event_id):
        """
        Fetches and returns the details of a specific event.
        """
        event = get_object_or_404(Event, id=event_id, organizer__user=request.user)
        data = {
            "id": event.id,
            "name": event.name,
            "description": event.description,
            "date": event.date,
            "time": event.time,
            "is_completed": event.is_completed,
            "accept_registrations": event.accept_registrations,
        }
        return JsonResponse(data)

    def put(self, request, event_id):
        """
        Updates the details of a specific event.
        """
        event = get_object_or_404(Event, id=event_id, organizer__user=request.user)
        try:
            data = json.loads(request.body)
            event.name = data.get("name", event.name)
            event.description = data.get("description", event.description)
            event.date = data.get("date", event.date)
            event.time = data.get("time", event.time)
            event.is_completed = data.get("is_completed", event.is_completed)
            event.accept_registrations = data.get("accept_registrations", event.accept_registrations)
            event.save()
            return JsonResponse({"message": "Event updated successfully!"})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)