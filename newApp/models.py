from django.db import models
from django.urls import reverse


class University(models.Model):
    name = models.CharField(max_length=40)
    location = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.name}"


class Student(models.Model):
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    identification_code = models.CharField(max_length=8)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
