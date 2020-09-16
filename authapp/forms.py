from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms.utils import ValidationError

from .models import User


class TeacherSignUpForm(UserCreationForm):
    user_type1 = forms.BooleanField(required=False)
    user_type2 = forms.BooleanField(required=False)
    user_type3 = forms.BooleanField(required=False)
    class Meta(UserCreationForm.Meta):
        model = User
    
    def clean(self):
        cleaned_data = super().clean()
        user_type1 = cleaned_data.get("user_type1")
        user_type2 = cleaned_data.get("user_type2")
        user_type3 = cleaned_data.get("user_type3")

        if (user_type1 or user_type2 or user_type3) == False:
            raise ValidationError(
                "Please choose at least one user type "
            )
    def save(self, commit=True):
        data = self.cleaned_data
        user = super().save(commit=False)
        user.user_type1=data['user_type1']
        user.user_type2=data['user_type2']
        user.user_type3=data['user_type3']
        if commit:
            user.save()
        return user


