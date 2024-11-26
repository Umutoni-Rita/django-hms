from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib.auth import authenticate, login
from patients.models import Patient
from doctors.models import Doctor
from appointments.models import Appointment

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            # Log the user in after registration
            user = authenticate(username=new_user.username, password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
            return redirect('')  # Redirect to some page after successful registration
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

def home(request):
    return render(request, 'base.html')


def dashboard(request):
    doctor_count = Doctor.objects.count()
    patient_count = Patient.objects.count()
    appointment_count = Appointment.objects.count()

    context = {
        'doctor_count': doctor_count,
        'patient_count': patient_count,
        'appointment_count': appointment_count,
    }

    return render(request, 'dashboard.html', context)


