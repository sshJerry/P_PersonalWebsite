from django import forms
from .models import CCSUMajors


class ProjectForm(forms.ModelForm):
    class Meta:
        model = CCSUMajors
        fields = '__all__'
