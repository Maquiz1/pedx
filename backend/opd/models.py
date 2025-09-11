from django.db import models
from patients.models import Patient


class OutPatient(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE)
    registration_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[("Active", "Active"), ("Discharged", "Discharged")])

    def __str__(self):
        return f"OPD - {self.patient}"
