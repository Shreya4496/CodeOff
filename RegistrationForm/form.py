from django import forms

from django.forms import ModelForm, Textarea
from .models import User


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'