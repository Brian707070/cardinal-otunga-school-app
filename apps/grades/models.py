from django.db import models
from apps.students.models import Student

class Subject(models.Model):
    """Subject model."""
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)
    description = models.TextField(blank=True, null=True)
    
    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name


class Grade(models.Model):
    """Grade/Score model."""
    TERM_CHOICES = (
        ('1', 'Term 1'),
        ('2', 'Term 2'),
        ('3', 'Term 3'),
    )
    
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='grades')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    score = models.DecimalField(max_digits=5, decimal_places=2)
    marks_obtained = models.IntegerField()
    marks_total = models.IntegerField()
    term = models.CharField(max_length=1, choices=TERM_CHOICES)
    year = models.IntegerField()
    
    remarks = models.TextField(blank=True, null=True)
    teacher_name = models.CharField(max_length=200, blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-year', '-term', 'subject']
        unique_together = ('student', 'subject', 'term', 'year')
    
    def __str__(self):
        return f"{self.student.first_name} - {self.subject.name} ({self.term}/{self.year})"


class ReportCard(models.Model):
    """Report card model."""
    TERM_CHOICES = (
        ('1', 'Term 1'),
        ('2', 'Term 2'),
        ('3', 'Term 3'),
    )
    
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='report_cards')
    term = models.CharField(max_length=1, choices=TERM_CHOICES)
    year = models.IntegerField()
    
    comments = models.TextField(blank=True, null=True)
    class_position = models.IntegerField(blank=True, null=True)
    class_size = models.IntegerField(blank=True, null=True)
    
    overall_score = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    overall_grade = models.CharField(max_length=2, blank=True, null=True)  # A+, A, B+, etc.
    
    issued_date = models.DateField(auto_now_add=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-year', '-term']
        unique_together = ('student', 'term', 'year')
    
    def __str__(self):
        return f"Report Card - {self.student.first_name} ({self.term}/{self.year})"
