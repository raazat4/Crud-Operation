from dataclasses import fields
from django import forms
from .models import Student

class AddStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ("name", "roll", "address", "institute")
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'roll':forms.NumberInput(attrs={'class':'form-control'}),
            'address':forms.TextInput(attrs={'class':'form-control'}),
            'institute':forms.TextInput(attrs={'class':'form-control'})
        }
        