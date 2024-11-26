from django.shortcuts import render, redirect
from .models import Patient
from .forms import PatientForm
# from django.contrib.auth.decorators import login_required

# Read Patients
# @login_required(login_url='/login/')
def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'patients/patient_list.html', {'patients': patients})

# Create Patient
def patient_create(request):
    if request.method == "POST":
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient_list')
    else:
        form = PatientForm()
    return render(request, 'patients/patient_form.html', {'form': form})

# Update Patient
def patient_update(request, id):
    patient = Patient.objects.get(id=id)
    if request.method == "POST":
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('patient_list')
    else:
        form = PatientForm(instance=patient)
    return render(request, 'patients/patient_form.html', {'form': form})

# Delete Patient
def patient_delete(request, id):
    patient = Patient.objects.get(id=id)
    if request.method == "POST":
        patient.delete()
        return redirect('patient_list')
    return render(request, 'patients/patient_delete.html', {'patient': patient})
