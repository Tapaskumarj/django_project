from django import forms
from registerapp.models import crud_student


class DateInput(forms.DateInput):
   input_type = 'date'

class studentForm(forms.ModelForm):
    doj = forms.DateField(widget=DateInput)
    dob = forms.DateField(widget=DateInput)
    gender: forms.ChoiceField(widget=forms.RadioSelect())
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model= crud_student
        fields='__all__'
