from django import forms
from django.db import models
from django.core.validators import RegexValidator


class Employee(models.Model):
    Gender_Choices = [
        ('M','Male'),
        ('F','Female'),
        ('O','Other'),
    ]

    phone_num = RegexValidator(regex=r'^\d{10}$' , message="Mobile Number must be exactly 10 digits.")
    name = models.CharField(max_length=60)
    gender = models.CharField(max_length=10, choices=Gender_Choices, verbose_name="Gender", null=True, blank=True)
    mob_num = models.CharField(validators=[phone_num], max_length=10)
    email = models.EmailField()
    address = models.TextField()
    salary = models.FloatField()
    designation = models.CharField()
    photo = models.ImageField(upload_to='employee_photos', null=True, blank=True)

    def __str__(self):
        return self.name
    