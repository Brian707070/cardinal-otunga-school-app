from django.contrib import admin
from .models import Attendance, AttendanceSummary

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('student', 'date', 'status')
    list_filter = ('date', 'status')
    search_fields = ('student__first_name', 'student__last_name')


@admin.register(AttendanceSummary)
class AttendanceSummaryAdmin(admin.ModelAdmin):
    list_display = ('student', 'year', 'attendance_percentage')
    list_filter = ('year',)
    search_fields = ('student__first_name', 'student__last_name')
