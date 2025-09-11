from django.db import models
from patients.models import Patient


class Diagnosis(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    condition = models.CharField(max_length=200)
    date_diagnosed = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.condition} ({self.patient})"


class TreatmentPlan(models.Model):
    diagnosis = models.ForeignKey(Diagnosis, on_delete=models.CASCADE, related_name="treatments")
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"Treatment for {self.diagnosis.condition}"
