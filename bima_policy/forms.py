from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    full_name = forms.CharField(max_length=63)
    password = forms.CharField(max_length=63, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['full_name','password']