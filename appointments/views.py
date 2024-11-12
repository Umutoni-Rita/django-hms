from django.shortcuts import render, redirect
from .models import Appointment
from .forms import AppointmentForm

# Read Appointments
def appointment_list(request):
    appointments = Appointment.objects.all()
    return render(request, 'appointments/appointment_list.html', {'appointments': appointments})

# Create Appointment
def appointment_create(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointment_list')
    else:
        form = AppointmentForm()
    return render(request, 'appointments/appointment_form.html', {'form': form})

# Update Appointment
def appointment_update(request, id):
    appointment = Appointment.objects.get(id=id)
    if request.method == "POST":
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('appointment_list')
    else:
        form = AppointmentForm(instance=appointment)
    return render(request, 'appointments/appointment_form.html', {'form': form})

# Delete Appointment
def appointment_delete(request, id):
    appointment = Appointment.objects.get(id=id)
    if request.method == "POST":
        appointment.delete()
        return redirect('appointment_list')
    return render(request, 'appointments/appointment_delete.html', {'appointment': appointment})
