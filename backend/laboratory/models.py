from django.db import models
from patients.models import Patient


class LabTest(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    test_name = models.CharField(max_length=100)
    requested_date = models.DateField(auto_now_add=True)
    result = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.test_name} for {self.patient}"
