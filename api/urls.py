from django.urls import path, include
from .views  import StudentListView
from .views      import ClassperiodListView


urlpatterns = [
    path('student/', StudentListView.as_view(), name = 'Student_list_view'),
    path('classperiod/', ClassperiodListView.as_view(), name = 'classperiod_list_view')
]