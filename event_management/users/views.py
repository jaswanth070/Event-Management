from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import get_user_model
from .models import Organizer, Participant, Volunteer, Event


# Role Selection View
def role_selection(request):
    if request.method == 'POST':
        role = request.POST.get('role')
        if role == 'organizer':
            return redirect('organizer_register')
        elif role == 'participant':
            return redirect('participant_register')
        elif role == 'volunteer':
            return redirect('volunteer_register')
        else:
            messages.error(request, 'Invalid role selected.')
            return redirect('role_selection')
    return render(request, 'Registration/role_selection.html')


# Organizer Registration View
def organizer_register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        phone_number = request.POST.get('phone_number')
        institute = request.POST.get('institute')

        # Validate data
        if password1 != password2:
            messages.error(request, 'Passwords do not match.')
            return redirect('organizer_register')

        if get_user_model().objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return redirect('organizer_register')

        if get_user_model().objects.filter(email=email).exists():
            messages.error(request, 'Email already exists.')
            return redirect('organizer_register')

        # Create the UserProfile
        user_profile = get_user_model().objects.create_user(username=username, email=email, password=password1)
        user_profile.phone_number = phone_number
        user_profile.institute = institute
        user_profile.role = 'organizer'
        user_profile.save()

        # Create the Organizer profile using the UserProfile instance
        organizer = Organizer(user=user_profile)  # Correct assignment of UserProfile instance
        organizer.save()

        messages.success(request, 'Organizer account created successfully!')
        return redirect('login')

    return render(request, 'Registration/organizer.html')


# Participant Registration View
def participant_register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        phone_number = request.POST.get('phone_number')
        institute = request.POST.get('institute')

        # Validate data
        if password1 != password2:
            messages.error(request, 'Passwords do not match.')
            return redirect('participant_register')

        if get_user_model().objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return redirect('participant_register')

        if get_user_model().objects.filter(email=email).exists():
            messages.error(request, 'Email already exists.')
            return redirect('participant_register')

        # Create the UserProfile
        user_profile = get_user_model().objects.create_user(username=username, email=email, password=password1)
        user_profile.phone_number = phone_number
        user_profile.institute = institute
        user_profile.role = 'participant'
        user_profile.save()

        # Create the Participant profile using the UserProfile instance
        participant = Participant(user=user_profile)  # Correct assignment of UserProfile instance
        participant.save()

        messages.success(request, 'Participant account created successfully!')
        return redirect('login')

    return render(request, 'Registration/participant.html')


# Volunteer Registration View
def volunteer_register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        phone_number = request.POST.get('phone_number')
        institute = request.POST.get('institute')

        # Validate data
        if password1 != password2:
            messages.error(request, 'Passwords do not match.')
            return redirect('volunteer_register')

        if get_user_model().objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return redirect('volunteer_register')

        if get_user_model().objects.filter(email=email).exists():
            messages.error(request, 'Email already exists.')
            return redirect('volunteer_register')

        # Create the UserProfile
        user_profile = get_user_model().objects.create_user(username=username, email=email, password=password1)
        user_profile.phone_number = phone_number
        user_profile.institute = institute
        user_profile.role = 'volunteer'
        user_profile.save()

        # Create the Volunteer profile using the UserProfile instance
        volunteer = Volunteer(user=user_profile)  # Correct assignment of UserProfile instance
        volunteer.save()

        messages.success(request, 'Volunteer account created successfully!')
        return redirect('login')

    return render(request, 'Registration/volunteer.html')
