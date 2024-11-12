from django import forms
from .models import Doctor

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['first_name', 'last_name', 'category', 'experience_years', 'contact_number', 'email']
        
