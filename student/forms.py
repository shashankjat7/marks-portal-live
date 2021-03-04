from django import forms
from .models import student

class submitMarksForm(forms.ModelForm):

    class Meta:
        model = student
        fields = ('roll_no','name','marks_maths','marks_chemistry','marks_physics','total','percentage')
