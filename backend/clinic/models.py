from django.db import models
from patients.models import Patient


class ClinicVisit(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    clinic_name = models.CharField(max_length=100)
    visit_date = models.DateField(auto_now_add=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.clinic_name} visit - {self.patient}"
