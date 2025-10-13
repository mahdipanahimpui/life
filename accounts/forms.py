from django import forms
from .models import User
from django.contrib.auth.forms import ReadOnlyPasswordHashField

class UserCreationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('phone_number', )


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(help_text= "<a href=\"../password/\">change password</a>")
    class Meta:
        model = User
        fields = ('phone_number', 'password', 'last_login')




class UserRegistrationForm(forms.Form):

    phone_number = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'phone',
            'placeholder': '*********09',
            'pattern': '[0-9]{11}',
            'maxlength': '11',
            'required': 'required'
        })
    )




class VerifyCodeForm(forms.Form):
    code = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'single-otp-input',
            'id': 'otp',
            'maxlength': '5',
            'inputmode': 'numeric',
            'pattern': "[0-9]*",
            'placeholder': '*****'
        })
    )


