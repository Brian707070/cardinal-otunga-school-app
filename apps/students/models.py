from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    """Student model for Cardinal Otunga School."""
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    
    admission_number = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    
    # Address information
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    postal_code = models.CharField(max_length=20, blank=True, null=True)
    
    # Academic information
    current_class = models.CharField(max_length=50, blank=True, null=True)
    date_enrolled = models.DateField(auto_now_add=True)
    
    # Parent/Guardian information
    parent_name = models.CharField(max_length=200, blank=True, null=True)
    parent_email = models.EmailField(blank=True, null=True)
    parent_phone = models.CharField(max_length=20, blank=True, null=True)
    
    # Account
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['last_name', 'first_name']
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.admission_number})"


class SchoolInfo(models.Model):
    """School information model."""
    school_name = models.CharField(max_length=200, default='Cardinal Otunga National School Mosocho')
    motto = models.CharField(max_length=500, blank=True, null=True)
    established_year = models.IntegerField(blank=True, null=True)
    principal_name = models.CharField(max_length=200, blank=True, null=True)
    principal_email = models.EmailField(blank=True, null=True)
    principal_phone = models.CharField(max_length=20, blank=True, null=True)
    
    school_email = models.EmailField(blank=True, null=True)
    school_phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    
    # Using FileField to avoid external Pillow dependency
    logo = models.FileField(upload_to='school/', blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.school_name
