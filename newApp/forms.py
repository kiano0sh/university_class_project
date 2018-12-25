from django import forms
from .models import *


class UniversityModelForm(forms.ModelForm):
    class Meta:
        model = University
        fields = [
            'name',
            'location'
        ]


class StudentModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(StudentModelForm, self).__init__(*args, **kwargs)
        self.fields['university'].widget.attrs.update({'class': 'browser-default'})

    class Meta:
        model = Student
        fields = [
            'university',
            'first_name',
            'last_name',
            'identification_code'
        ]
