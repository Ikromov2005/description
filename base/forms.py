from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='First Name')
    last_name = forms.CharField(max_length=30, required=True, help_text='Last Name')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2')