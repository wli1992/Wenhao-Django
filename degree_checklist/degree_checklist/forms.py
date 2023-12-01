# forms.py

from django import forms
from .models import DegreeProgram, Course

class DegreeProgramForm(forms.ModelForm):
    class Meta:
        model = DegreeProgram
        fields = '__all__'

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
        