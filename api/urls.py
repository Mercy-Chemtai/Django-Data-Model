from django.urls import path 
from .views  import StudentListView
from .views  import ClassperiodListView
from .views  import TeacherListView
from .views  import ClassesListView
from .views  import CourseListView 
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', StudentListView.as_view(), name = 'Student_list_view'),
    path('classperiod/', ClassperiodListView.as_view(), name = 'classperiod_list_view'),
    path('course/', CourseListView.as_view(), name = 'course_list_view'),
    path('classes/', ClassesListView.as_view(), name = 'classes_list_view'),
    path('teacher/', TeacherListView.as_view(), name = 'teacher_list_view')
]