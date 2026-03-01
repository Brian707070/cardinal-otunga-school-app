from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import (
    StudentViewSet, SchoolInfoViewSet, SubjectViewSet,
    GradeViewSet, ReportCardViewSet, AttendanceViewSet,
    AttendanceSummaryViewSet, AnnouncementViewSet,
    EventCalendarViewSet, MessageViewSet, ConversationViewSet,
    FeedbackViewSet
)

router = DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'school-info', SchoolInfoViewSet)
router.register(r'subjects', SubjectViewSet)
router.register(r'grades', GradeViewSet)
router.register(r'report-cards', ReportCardViewSet)
router.register(r'attendance', AttendanceViewSet)
router.register(r'attendance-summary', AttendanceSummaryViewSet)
router.register(r'announcements', AnnouncementViewSet)
router.register(r'events', EventCalendarViewSet)
router.register(r'messages', MessageViewSet, basename='message')
router.register(r'conversations', ConversationViewSet, basename='conversation')
router.register(r'feedback', FeedbackViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
