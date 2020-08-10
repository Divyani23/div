from App.models import StudentData
from django import forms
class insert_Student(forms.ModelForm):
    class Meta:
        model=StudentData
        fields='__all__'
