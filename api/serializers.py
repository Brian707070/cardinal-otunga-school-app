from rest_framework import serializers
from apps.students.models import Student, SchoolInfo
from apps.grades.models import Subject, Grade, ReportCard
from apps.attendance.models import Attendance, AttendanceSummary
from apps.announcements.models import Announcement, EventCalendar
from apps.communication.models import Message, Conversation, ConversationMessage, Feedback
from django.contrib.auth.models import User


# Student Serializers
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = [
            'id', 'admission_number', 'first_name', 'last_name', 'date_of_birth',
            'gender', 'email', 'phone_number', 'address', 'city', 'postal_code',
            'current_class', 'date_enrolled', 'parent_name', 'parent_email',
            'parent_phone', 'is_active'
        ]


class SchoolInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolInfo
        fields = [
            'id', 'school_name', 'motto', 'established_year', 'principal_name',
            'principal_email', 'principal_phone', 'school_email', 'school_phone',
            'address', 'website', 'logo'
        ]


# Grade Serializers
class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'name', 'code', 'description']


class GradeSerializer(serializers.ModelSerializer):
    subject_name = serializers.SerializerMethodField()
    student_name = serializers.SerializerMethodField()

    class Meta:
        model = Grade
        fields = [
            'id', 'student', 'student_name', 'subject', 'subject_name', 'score',
            'marks_obtained', 'marks_total', 'term', 'year', 'remarks', 'teacher_name'
        ]

    def get_subject_name(self, obj):
        return obj.subject.name

    def get_student_name(self, obj):
        return f"{obj.student.first_name} {obj.student.last_name}"


class ReportCardSerializer(serializers.ModelSerializer):
    student_name = serializers.SerializerMethodField()

    class Meta:
        model = ReportCard
        fields = [
            'id', 'student', 'student_name', 'term', 'year', 'comments',
            'class_position', 'class_size', 'overall_score', 'overall_grade', 'issued_date'
        ]

    def get_student_name(self, obj):
        return f"{obj.student.first_name} {obj.student.last_name}"


# Attendance Serializers
class AttendanceSerializer(serializers.ModelSerializer):
    student_name = serializers.SerializerMethodField()

    class Meta:
        model = Attendance
        fields = [
            'id', 'student', 'student_name', 'date', 'status', 'remarks', 'recorded_by'
        ]

    def get_student_name(self, obj):
        return f"{obj.student.first_name} {obj.student.last_name}"


class AttendanceSummarySerializer(serializers.ModelSerializer):
    student_name = serializers.SerializerMethodField()

    class Meta:
        model = AttendanceSummary
        fields = [
            'id', 'student', 'student_name', 'year', 'total_days', 'days_present',
            'days_absent', 'days_late', 'days_excused', 'attendance_percentage'
        ]

    def get_student_name(self, obj):
        return f"{obj.student.first_name} {obj.student.last_name}"


# Announcement Serializers
class AnnouncementSerializer(serializers.ModelSerializer):
    created_by_name = serializers.SerializerMethodField()

    class Meta:
        model = Announcement
        fields = [
            'id', 'title', 'content', 'summary', 'priority', 'category',
            'created_by', 'created_by_name', 'image', 'published_date', 'is_active'
        ]

    def get_created_by_name(self, obj):
        return obj.created_by.username if obj.created_by else None


class EventCalendarSerializer(serializers.ModelSerializer):
    created_by_name = serializers.SerializerMethodField()

    class Meta:
        model = EventCalendar
        fields = [
            'id', 'title', 'description', 'event_date', 'end_date', 'location',
            'category', 'created_by', 'created_by_name', 'is_active'
        ]

    def get_created_by_name(self, obj):
        return obj.created_by.username if obj.created_by else None


# Communication Serializers
class MessageSerializer(serializers.ModelSerializer):
    sender_username = serializers.SerializerMethodField()
    recipient_username = serializers.SerializerMethodField()

    class Meta:
        model = Message
        fields = [
            'id', 'sender', 'sender_username', 'recipient', 'recipient_username',
            'subject', 'content', 'is_read', 'read_at', 'sent_at'
        ]

    def get_sender_username(self, obj):
        return obj.sender.username

    def get_recipient_username(self, obj):
        return obj.recipient.username


class ConversationMessageSerializer(serializers.ModelSerializer):
    sender_username = serializers.SerializerMethodField()

    class Meta:
        model = ConversationMessage
        fields = ['id', 'conversation', 'sender', 'sender_username', 'content', 'sent_at']

    def get_sender_username(self, obj):
        return obj.sender.username


class ConversationSerializer(serializers.ModelSerializer):
    messages = ConversationMessageSerializer(many=True, read_only=True)
    created_by_name = serializers.SerializerMethodField()
    participant_count = serializers.SerializerMethodField()

    class Meta:
        model = Conversation
        fields = [
            'id', 'title', 'description', 'participants', 'created_by', 'created_by_name',
            'created_at', 'updated_at', 'is_active', 'messages', 'participant_count'
        ]

    def get_created_by_name(self, obj):
        return obj.created_by.username if obj.created_by else None

    def get_participant_count(self, obj):
        return obj.participants.count()


class FeedbackSerializer(serializers.ModelSerializer):
    submitted_by_username = serializers.SerializerMethodField()
    student_name = serializers.SerializerMethodField()

    class Meta:
        model = Feedback
        fields = [
            'id', 'student', 'student_name', 'submitted_by', 'submitted_by_username',
            'feedback_type', 'subject', 'message', 'status', 'response', 'submitted_at', 'resolved_at'
        ]

    def get_submitted_by_username(self, obj):
        return obj.submitted_by.username if obj.submitted_by else None

    def get_student_name(self, obj):
        return f"{obj.student.first_name} {obj.student.last_name}" if obj.student else None
