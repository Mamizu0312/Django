from django import forms
from .models import User

class LoginForm(forms.Form):
    user_id = forms.CharField(label="ID:")
    password = forms.CharField(label="password: ")
