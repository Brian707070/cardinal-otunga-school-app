from django.contrib import admin
from .models import Announcement, EventCalendar

@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('title', 'priority', 'category', 'published_date', 'is_active')
    list_filter = ('priority', 'category', 'is_active', 'published_date')
    search_fields = ('title', 'content')


@admin.register(EventCalendar)
class EventCalendarAdmin(admin.ModelAdmin):
    list_display = ('title', 'event_date', 'category', 'location', 'is_active')
    list_filter = ('event_date', 'category', 'is_active')
    search_fields = ('title', 'description', 'location')
