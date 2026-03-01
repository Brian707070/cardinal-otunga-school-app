from django.contrib import admin
from .models import Subject, Grade, ReportCard

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')
    search_fields = ('name', 'code')


@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ('student', 'subject', 'score', 'term', 'year')
    list_filter = ('term', 'year', 'subject')
    search_fields = ('student__first_name', 'student__last_name', 'subject__name')


@admin.register(ReportCard)
class ReportCardAdmin(admin.ModelAdmin):
    list_display = ('student', 'term', 'year', 'overall_score', 'class_position')
    list_filter = ('term', 'year')
    search_fields = ('student__first_name', 'student__last_name')
