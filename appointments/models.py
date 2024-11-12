from django.db import models
from doctors.models import Doctor
from patients.models import Patient

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_date = models.DateTimeField()
    reason = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Appointment with {self.doctor} for {self.patient} on {self.appointment_date}"
