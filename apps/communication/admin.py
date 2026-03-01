from django.contrib import admin
from .models import Message, Conversation, ConversationMessage, Feedback

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'recipient', 'subject', 'is_read', 'sent_at')
    list_filter = ('is_read', 'sent_at')
    search_fields = ('sender__username', 'recipient__username', 'subject')


@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_by', 'created_at', 'is_active')
    list_filter = ('created_at', 'is_active')
    search_fields = ('title', 'description')


@admin.register(ConversationMessage)
class ConversationMessageAdmin(admin.ModelAdmin):
    list_display = ('conversation', 'sender', 'sent_at')
    list_filter = ('sent_at',)
    search_fields = ('sender__username', 'conversation__title', 'content')


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('feedback_type', 'subject', 'status', 'submitted_at')
    list_filter = ('feedback_type', 'status', 'submitted_at')
    search_fields = ('subject', 'message', 'submitted_by__username')
