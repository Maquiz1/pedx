from django.db import models
from patients.models import Patient
from staff.models import Staff
from patients.models import Patient
from django.core.exceptions import ValidationError


class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Staff, on_delete=models.SET_NULL, null=True, limit_choices_to={'role__name': 'Doctor'})
    date = models.DateTimeField()
    reason = models.TextField()

    def __str__(self):
        return f"Appointment for {self.patient} with {self.doctor}"

class ClinicVisit(models.Model):
    VISIT_TYPE_CHOICES = [
        ("enrollment", "Enrollment"),
        ("follow_up", "Follow-up"),
    ]

    FOLLOW_UP_TYPE_CHOICES = [
        ("scheduled", "Scheduled"),
        ("unscheduled", "Unscheduled"),
    ]

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    clinic_name = models.CharField(max_length=100)
    visit_date = models.DateField(auto_now_add=True)
    visit_type = models.CharField(max_length=20, choices=VISIT_TYPE_CHOICES)
    follow_up_type = models.CharField(
        max_length=20,
        choices=FOLLOW_UP_TYPE_CHOICES,
        blank=True,
        null=True,
        help_text="Only required if visit type is Follow-up"
    )
    reason = models.TextField(
        blank=True,
        null=True,
        help_text="Required if follow-up is unscheduled"
    )
    notes = models.TextField(blank=True, null=True)

    def clean(self):
        # Ensure follow_up_type is only set if visit_type is follow_up
        if self.visit_type != "follow_up":
            self.follow_up_type = None
            self.reason = None
        # If follow-up is unscheduled, reason is required
        if self.visit_type == "follow_up" and self.follow_up_type == "unscheduled" and not self.reason:
            raise ValidationError({'reason': "Reason is required for unscheduled follow-up visits."})

    def save(self, *args, **kwargs):
        self.full_clean()  # Calls clean() before saving
        super().save(*args, **kwargs)

    def __str__(self):
        if self.visit_type == "follow_up":
            return f"{self.get_visit_type_display()} ({self.get_follow_up_type_display()}) - {self.patient}"
        return f"{self.get_visit_type_display()} visit - {self.patient}"

