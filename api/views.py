from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny

# Default to allowing any user to interact with API resources
PUBLIC_PERMISSION = AllowAny
from apps.students.models import Student, SchoolInfo
from apps.grades.models import Subject, Grade, ReportCard
from apps.attendance.models import Attendance, AttendanceSummary
from apps.announcements.models import Announcement, EventCalendar
from apps.communication.models import Message, Conversation, ConversationMessage, Feedback
from api.serializers import (
    StudentSerializer, SchoolInfoSerializer, SubjectSerializer,
    GradeSerializer, ReportCardSerializer, AttendanceSerializer,
    AttendanceSummarySerializer, AnnouncementSerializer,
    EventCalendarSerializer, MessageSerializer, ConversationSerializer,
    FeedbackSerializer, ConversationMessageSerializer
)


class StudentViewSet(viewsets.ModelViewSet):
    """API endpoint for Student operations."""
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [AllowAny]
    
    @action(detail=True, methods=['get'])
    def by_admission(self, request, pk=None):
        """Get student by admission number."""
        try:
            student = Student.objects.get(admission_number=pk)
        except Student.DoesNotExist:
            return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(student)
        return Response(serializer.data)


class SchoolInfoViewSet(viewsets.ReadOnlyModelViewSet):
    """API endpoint for School Information."""
    queryset = SchoolInfo.objects.all()
    serializer_class = SchoolInfoSerializer
    permission_classes = [AllowAny]


class SubjectViewSet(viewsets.ReadOnlyModelViewSet):
    """API endpoint for Subjects."""
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [AllowAny]


class GradeViewSet(viewsets.ReadOnlyModelViewSet):
    """API endpoint for Grades."""
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer
    permission_classes = [AllowAny]
    filterset_fields = ['student', 'subject', 'term', 'year']
    
    @action(detail=False, methods=['get'])
    def by_student(self, request):
        """Get all grades for a specific student."""
        student_id = request.query_params.get('student_id')
        if not student_id:
            return Response({'error': 'student_id parameter required'}, status=status.HTTP_400_BAD_REQUEST)
        
        grades = Grade.objects.filter(student_id=student_id)
        serializer = self.get_serializer(grades, many=True)
        return Response(serializer.data)


class ReportCardViewSet(viewsets.ReadOnlyModelViewSet):
    """API endpoint for Report Cards."""
    queryset = ReportCard.objects.all()
    serializer_class = ReportCardSerializer
    permission_classes = [AllowAny]
    filterset_fields = ['student', 'term', 'year']


class AttendanceViewSet(viewsets.ModelViewSet):
    """API endpoint for Attendance."""
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = [AllowAny]
    filterset_fields = ['student', 'date', 'status']


class AttendanceSummaryViewSet(viewsets.ReadOnlyModelViewSet):
    """API endpoint for Attendance Summary."""
    queryset = AttendanceSummary.objects.all()
    serializer_class = AttendanceSummarySerializer
    permission_classes = [AllowAny]


class AnnouncementViewSet(viewsets.ModelViewSet):
    """API endpoint for Announcements."""
    queryset = Announcement.objects.filter(is_active=True)
    serializer_class = AnnouncementSerializer
    permission_classes = [AllowAny]
    filterset_fields = ['priority', 'category']
    ordering_fields = ['-published_date']


class EventCalendarViewSet(viewsets.ModelViewSet):
    """API endpoint for Event Calendar."""
    queryset = EventCalendar.objects.filter(is_active=True)
    serializer_class = EventCalendarSerializer
    permission_classes = [AllowAny]
    filterset_fields = ['category']
    ordering_fields = ['event_date']


class MessageViewSet(viewsets.ModelViewSet):
    """API endpoint for Messages.  Open to all users as requested."""
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [PUBLIC_PERMISSION]
    
    @action(detail=False, methods=['get'])
    def inbox(self, request):
        """Get all messages received by the current user."""
        messages = Message.objects.filter(recipient=request.user)
        serializer = self.get_serializer(messages, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def sent(self, request):
        """Get all messages sent by the current user."""
        messages = Message.objects.filter(sender=request.user)
        serializer = self.get_serializer(messages, many=True)
        return Response(serializer.data)


class ConversationViewSet(viewsets.ModelViewSet):
    """API endpoint for Conversations.  Public access granted."""
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    permission_classes = [PUBLIC_PERMISSION]
    
    @action(detail=True, methods=['post'])
    def add_message(self, request, pk=None):
        """Add a message to a conversation."""
        conversation = self.get_object()
        serializer = ConversationMessageSerializer(data={
            'conversation': conversation.id,
            'sender': request.user.id,
            'content': request.data.get('content')
        })
        if serializer.is_valid():
            serializer.save()
            # Update conversation updated_at
            conversation.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FeedbackViewSet(viewsets.ModelViewSet):
    """API endpoint for Feedback/Complaints."""
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = [AllowAny]
    filterset_fields = ['feedback_type', 'status', 'student']
