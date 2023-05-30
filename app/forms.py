from django import forms
from app.models import *
from django.core import validators

def validsname(sname):
    if len(sname)<=3:
        raise forms.ValidationError('name should contain above 3 letters..')

class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=['sname','sid','tname']
        validators=[validsname]