from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404,render
import json
from .models import Event
from users.models import Organizer

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
            "location": event.location,
            "category": event.category,
            "fee": event.fee,
            "capacity": event.capacity,
            "is_completed": event.is_completed,
            "accept_registrations": event.accept_registrations,
            "participants_count": event.participants.count(),
            "image_url": event.image.url if event.image else None,
        }
        return JsonResponse(data)

    def put(self, request, event_id):
        """
        Updates the details of a specific event.
        """
        event = get_object_or_404(Event, id=event_id, organizer__user=request.user)
        try:
            data = json.loads(request.body)
            # Update event fields with provided data or retain current values
            event.name = data.get("name", event.name)
            event.description = data.get("description", event.description)
            event.date = data.get("date", event.date)
            event.time = data.get("time", event.time)
            event.location = data.get("location", event.location)
            event.category = data.get("category", event.category)
            event.fee = data.get("fee", event.fee)
            event.capacity = data.get("capacity", event.capacity)
            event.is_completed = data.get("is_completed", event.is_completed)
            event.accept_registrations = data.get("accept_registrations", event.accept_registrations)
            event.save()
            return JsonResponse({"message": "Event updated successfully!"})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

def create_event(request):
    if request.method == "POST":
        try:
            organizer = Organizer.objects.get(user=request.user)

            event_data = request.POST
            image = request.FILES.get('event_image')  # Get uploaded image

            event = Event.objects.create(
                name=event_data["event_name"],
                description=event_data["event_description"],
                date=event_data["event_date"],
                time=event_data["event_time"],
                location=event_data["event_location"],
                category=event_data["event_category"],
                fee=event_data.get("event_fee", 0),
                capacity=event_data["event_capacity"],
                image=image,  # Save the uploaded image
                organizer=organizer
            )
            return JsonResponse({"message": "Event created successfully!"}, status=201)
        except KeyError as e:
            return JsonResponse({"error": f"Missing field: {str(e)}"}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    return render(request,"events/event_creation.html")