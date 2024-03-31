from django import forms
from .models import CustomUser
from django.forms import ModelForm, ImageField, Form, CharField, PasswordInput

# class UserRegistrationForm(forms.ModelForm):
#     class Meta:
#         model = CustomUser
#         fields = ['username', 'email', 'password']
#         widgets = {
#             'password': forms.PasswordInput(),
#         }

class UserRegisterForm(forms.ModelForm):
    password = CharField(max_length = 128, widget=PasswordInput)

    def save(self, commit=True):
        user = super().save(commit)
        user.set_password(self.cleaned_data["password"])
        user.save()
        return user

    class Meta:
        model = CustomUser
        fields = "__all__"




class UserLoginForm(Form):
    username = CharField(max_length=128)
    password = CharField(max_length=128, widget=PasswordInput)