from django import forms
from .models import Volunteer

class SignupForm(forms.Form):
    volunteer_name = forms.CharField(max_length=100)
    volunteer_email = forms.EmailField()
    volunteer_grade = forms.IntegerField(initial=1, min_value=1, max_value=12)
    volunteer_detail = forms.CharField(max_length=200)
