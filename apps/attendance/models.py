from django.db import models
from apps.students.models import Student

class Attendance(models.Model):
    """Attendance tracking model."""
    STATUS_CHOICES = (
        ('P', 'Present'),
        ('A', 'Absent'),
        ('L', 'Late'),
        ('E', 'Excused'),
    )
    
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='attendance_records')
    date = models.DateField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    remarks = models.TextField(blank=True, null=True)
    
    recorded_by = models.CharField(max_length=200, blank=True, null=True)
    recorded_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-date']
        unique_together = ('student', 'date')
    
    def __str__(self):
        return f"{self.student.first_name} - {self.date} ({self.status})"


class AttendanceSummary(models.Model):
    """Attendance summary model."""
    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name='attendance_summary')
    
    year = models.IntegerField()
    
    total_days = models.IntegerField(default=0)
    days_present = models.IntegerField(default=0)
    days_absent = models.IntegerField(default=0)
    days_late = models.IntegerField(default=0)
    days_excused = models.IntegerField(default=0)
    
    attendance_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-year']
    
    def __str__(self):
        return f"Attendance Summary - {self.student.first_name} ({self.year})"
