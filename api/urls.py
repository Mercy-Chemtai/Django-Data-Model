from django.urls import path
from django.contrib import admin
from .views import StudentListView, ClassperiodListView, CourseListView, ClassesListView, TeacherListView, StudentDetailView, ClassperiodDetailView, ClassesDetailView, CourseDetailView,TeacherDetailView,TeacherCourseAssignmentView,TeacherTimetableView

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('students/', StudentListView.as_view(), name='student_list_view'),
    path('classperiods/', ClassperiodListView.as_view(), name='classperiod_list_view'),  
    path('courses/', CourseListView.as_view(), name='course_list_view'),  
    path('classes/', ClassesListView.as_view(), name='classes_list_view'),
    path('teachers/', TeacherListView.as_view(), name='teacher_list_view'),  
    path('students/<int:id>/', StudentDetailView.as_view(), name='student_detail_view'),  
    path('classperiod/<int:id>/', ClassperiodDetailView.as_view(), name='classperiod_detail_view'), 
    path('classes/<int:id>/', ClassesDetailView.as_view(), name='classes_detail_view'), 
    path('teacher/<int:id>/', TeacherDetailView.as_view(), name='teacher_detail_view'), 
    path('course/<int:id>/', CourseDetailView.as_view(), name='course_detail_view'), 
    path('teachers/<int:teacher_id>/courses/', TeacherCourseAssignmentView.as_view()),
    path('teachers/<int:teacher_id>/timetable/', TeacherTimetableView.as_view()),
]