from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import University, Student
from .forms import UniversityModelForm, StudentModelForm


# Create your views here.

class UniversityCreateView(CreateView):
    queryset = University.objects.all()
    form_class = UniversityModelForm
    template_name = "newApp/university_create.html"
    success_url = '/new_app/university/list'


class UniversityListView(ListView):
    queryset = University.objects.all()
    template_name = "newApp/university_list.html"


class StudentsCreateView(CreateView):
    queryset = Student.objects.all()
    form_class = StudentModelForm
    template_name = "newApp/student_create.html"
    success_url = '/new_app/student/list'


class StudentsListView(ListView):
    queryset = Student.objects.all()
    template_name = "newApp/student_list.html"


