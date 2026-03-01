from django.contrib import admin
from .models import Student, SchoolInfo

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('admission_number', 'first_name', 'last_name', 'current_class', 'is_active')
    list_filter = ('current_class', 'is_active', 'date_enrolled')
    search_fields = ('admission_number', 'first_name', 'last_name', 'parent_email')
    fieldsets = (
        ('Personal Information', {
            'fields': ('admission_number', 'first_name', 'last_name', 'date_of_birth', 'gender', 'email', 'phone_number')
        }),
        ('Address', {
            'fields': ('address', 'city', 'postal_code')
        }),
        ('Academic Information', {
            'fields': ('current_class', 'date_enrolled')
        }),
        ('Parent/Guardian Information', {
            'fields': ('parent_name', 'parent_email', 'parent_phone')
        }),
        ('Account', {
            'fields': ('user', 'is_active')
        }),
    )


@admin.register(SchoolInfo)
class SchoolInfoAdmin(admin.ModelAdmin):
    list_display = ('school_name', 'principal_name', 'school_phone')
    fieldsets = (
        ('School Information', {
            'fields': ('school_name', 'motto', 'established_year', 'logo')
        }),
        ('Principal Information', {
            'fields': ('principal_name', 'principal_email', 'principal_phone')
        }),
        ('Contact Information', {
            'fields': ('school_email', 'school_phone', 'address', 'website')
        }),
    )
