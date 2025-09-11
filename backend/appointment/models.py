from django.db import models

# Create your models here.
class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.ForeignKey('departments.Department', on_delete=models.SET_NULL, null=True)
    specialty = models.CharField(max_length=100)
