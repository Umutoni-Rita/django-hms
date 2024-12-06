from django.shortcuts import render, redirect
from doctors.models import Doctor
from doctors.forms import DoctorForm
from django.core.paginator import Paginator
# from django.contrib.auth.decorators import login_required # type: ignore

# Read Doctors
# @login_required(login_url='/login/')


def doctor_list(request):
    doctor_list = Doctor.objects.all()  
    paginator = Paginator(doctor_list, 500)  

    page_number = request.GET.get('page')  
    page_obj = paginator.get_page(page_number)  
    return render(request, 'doctor_list.html', {'page_obj': page_obj})


# Create Doctor
def doctor_create(request):
    if request.method == "POST":
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('doctor_list')
    else:
        form = DoctorForm()
    return render(request, 'doctors/doctor_form.html', {'form': form})

# Update Doctor
def doctor_update(request, id):
    doctor = Doctor.objects.get(id=id)
    if request.method == "POST":
        form = DoctorForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect('doctor_list')
    else:
        form = DoctorForm(instance=doctor)
    return render(request, 'doctors/doctor_form.html', {'form': form})

# Delete Doctor
def doctor_delete(request, id):
    doctor = Doctor.objects.get(id=id)
    if request.method == "POST":
        doctor.delete()
        return redirect('doctor_list')
    return render(request, 'doctors/doctor_delete.html', {'doctor': doctor})


def home_view(request):
    return render(request, 'home.html')
