import time
from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404,render
import json
from .models import Event
from users.models import Organizer
from datetime import date,datetime
from django.core.exceptions import ValidationError


def validate_image(image):
    if image:
        # Check if the file is an image by its extension
        allowed_extensions = ['jpg', 'jpeg', 'png', 'gif']
        file_extension = image.name.split('.')[-1].lower()

        if file_extension not in allowed_extensions:
            raise ValidationError("Invalid file format. Only JPG, JPEG, PNG, and GIF are allowed.")
    return image

def create_event(request):
    if request.user.role != "organizer":
        return JsonResponse({"error": "Forbidden"}, status=403)
    if request.method == "POST":
        
        try:
            organizer = Organizer.objects.get(user=request.user)

            event_data = request.POST
            image = request.FILES.get('event_image')  # Get uploaded image
            if image:
                print(f"Image uploaded: {image.name}")
            else:
                print("No image uploaded")

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
                organizer=organizer,
                accept_registrations = True if event_data["event_accept_registrations"] == "True" else False
            )
            return JsonResponse({"status":"success","message": "Event created successfully!"}, status=201)
        except KeyError as e:
            return JsonResponse({ "status": "error","message": f"Missing field: {str(e)}"}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    today = date.today()
    return render(request,"events/event_creation.html", {"today":today})

def editEvent(request,event_id):
    if request.user.role != "organizer":
        return JsonResponse({"error": "Forbidden"}, status=403)
    if event.organizer.id != request.user.id:
        return JsonResponse({"error": "Forbidden"}, status=403)
    
    event = get_object_or_404(Event, id=event_id)

    if request.method == "POST":
        try:
            event_data = request.POST
            image = request.FILES.get('event_image') 
            image = validate_image(image) 
            event.name = event_data["event_name"]
            event.description = event_data["event_description"]
            event.date = event_data["event_date"]
            event.time = event_data["event_time"]
            event.location = event_data["event_location"]
            event.category = event_data["event_category"]
            event.fee = event_data.get("event_fee", 0)
            event.capacity = event_data["event_capacity"]
            event.is_completed = True if event_data.get("event_is_completed") == "on" else False
            if event_data.get("event_is_completed") == "on":
                event.accept_registrations = False
            else:
                event.accept_registrations = True if event_data.get("event_accept_registrations") == "on" else False
            
            
            if image:
                event.image = image  

            event.save()

            return JsonResponse({"status": "success", "message": "Event updated successfully!"}, status=200)
        except KeyError as e:
            return JsonResponse({"status": "error", "message": f"Missing field: {str(e)}"}, status=400)
        except ValidationError as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    
    
    event_time = event.time.strftime('%H:%M')
    today = date.today()

    return render(request, "events/edit_event.html", {
        "event": event,
        "today": today,
        "formatted_time": event_time,
        "image_url": event.image.url if event.image else None,
    })

@csrf_exempt
def deleteEvent(request,event_id):
    if request.user.role != "organizer":
        return JsonResponse({"error": "Forbidden"}, status=403)
    if request.method == "DELETE":
        try:
            event = get_object_or_404(Event, id=event_id)
            if event.organizer.id != request.user.id:
                return JsonResponse({"error": "Forbidden"}, status=403)

            event.delete()
            return JsonResponse({"message":"Event deleted successfully"},status=200)
        except Exception as e :
            return JsonResponse({"error":e},status=500)
    else:
        return JsonResponse({"error": "Invalid HTTP method. Use DELETE."}, status=405)

def editAccount(request):
    pass

def myevents(request):
    if request.user.role != "organizer":
        return JsonResponse({"error": "Forbidden"}, status=403)
    
    events = Event.objects.filter(organizer__user=request.user)
    events_count = events.count()
    for event in events:
        event.participant_count = event.participants.count()
        if event.is_completed:
            event.bg = "green"
        else:
            event.bg = "indigo"
    return render(request,"events/myevents.html",{"events":events,"events_count":events_count})




