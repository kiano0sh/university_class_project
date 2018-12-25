from django.urls import path
from .views import *

app_name = 'newApp'

urlpatterns = [
    path('student/create', StudentsCreateView.as_view(), name='create_student'),
    path('student/list', StudentsListView.as_view(), name='students_list'),
    path('university/create', UniversityCreateView.as_view(), name='create_university'),
    path('university/list', UniversityListView.as_view(), name='universities_list')
]
