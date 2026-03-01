from django.db import models
from django.contrib.auth.models import User

class Announcement(models.Model):
    """Announcement/News model."""
    PRIORITY_CHOICES = (
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('urgent', 'Urgent'),
    )
    
    title = models.CharField(max_length=200)
    content = models.TextField()
    summary = models.CharField(max_length=500, blank=True, null=True)
    
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium')
    category = models.CharField(max_length=100, blank=True, null=True)  # Academic, Events, Health, etc.
    
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    
    # Using FileField instead of ImageField avoids needing Pillow for validation
    image = models.FileField(upload_to='announcements/', blank=True, null=True)
    
    published_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['-published_date']
    
    def __str__(self):
        return self.title


class EventCalendar(models.Model):
    """School events calendar model."""
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    
    event_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    
    category = models.CharField(max_length=100, blank=True, null=True)  # Academic, Sports, Cultural, etc.
    
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['event_date']
    
    def __str__(self):
        return f"{self.title} - {self.event_date}"
