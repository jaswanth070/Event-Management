from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.contrib import messages
from .models import Organizer, Participant, Volunteer, UserProfile


def register(request):
    if request.method == "POST":
        role = request.POST.get('role')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        phone = request.POST.get('phone')
        institute = request.POST.get('institute', None)

        if password != confirm_password:
            return JsonResponse({"errors": ["Passwords do not match."]}, status=400)

        if UserProfile.objects.filter(username=username).exists():
            return JsonResponse({"errors": ["Username already exists."]}, status=400)

        if UserProfile.objects.filter(email=email).exists():
            return JsonResponse({"errors": ["Email is already registered."]}, status=400)

        # Create user profile
        user_profile = UserProfile.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            password=password,
        )
        user_profile.email = email
        user_profile.phone_number = phone
        user_profile.role = role
        if institute:
            user_profile.institute = institute
        user_profile.save()

        if role == "organizer":
            Organizer.objects.create(user=user_profile)
        elif role == "participant":
            Participant.objects.create(user=user_profile)
        elif role == "volunteer":
            Volunteer.objects.create(user=user_profile)

        return JsonResponse({
            "message": "Registration successful!",
            "redirect_url": "/login"
        })

    return render(request, 'register.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        role = request.POST.get('role')

        try:
            # Fetch the user from the UserProfile model
            user = UserProfile.objects.get(username=username)

            # Check if the password is valid and the role matches
            if user.check_password(password):
                if user.role == role:
                    login(request, user)  # Log the user in
                    return JsonResponse({
                        "message": "Login successful!",
                        "redirect_url": "/"  # Change to your dashboard/homepage
                    })
                else:
                    return JsonResponse({
                        "errors": ["Role mismatch. Please check your role selection."]
                    }, status=400)
            else:
                return JsonResponse({
                    "errors": ["Invalid password."]
                }, status=400)
        except UserProfile.DoesNotExist:
            return JsonResponse({
                "errors": ["Invalid username."]
            }, status=400)

    return render(request, "login.html")
