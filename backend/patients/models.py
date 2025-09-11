from django.db import models


class Patient(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=[("M", "Male"), ("F", "Female")])
    national_id = models.CharField(max_length=50, unique=True, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class ContactInfo(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE, related_name="contact")
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    address = models.TextField()

    def __str__(self):
        return self.phone


class Insurance(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="insurances")
    provider = models.CharField(max_length=100)
    policy_number = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.provider} - {self.policy_number}"
