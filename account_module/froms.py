from django.core import validators
from django import forms
from django.core.exceptions import ValidationError
from django.views import View


class RegisterForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(),
        label='ایمیل',
        validators=[
            validators.EmailValidator(),
            validators.MaxLengthValidator(100)
        ]
    )
    password = forms.CharField(
        widget=forms.PasswordInput(),
        label='کلمه عبور',
        validators=[
            validators.MaxLengthValidator(100)
        ]
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(),
        label='تکرار کلمه عبور',
        validators=[
            validators.MaxLengthValidator(100)
        ]
    )

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password == confirm_password:
            return confirm_password

        raise ValidationError('کلمه عبور و تکرار کلمه عبور مغایرت دارند')

class LoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(),
        label='ایمیل',
        validators=[
            validators.EmailValidator(),
            validators.MaxLengthValidator(100)
        ]
    )
    password = forms.CharField(
        widget=forms.PasswordInput(),
        label='کلمه عبور',
        validators = [
            validators.MaxLengthValidator(100)
    ]
    )

class ForgotPasswordForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(),
        label='ایمیل',
        validators=[
            validators.EmailValidator(),
            validators.MaxLengthValidator(100)
        ]
    )

class ResetPasswordForm(forms.Form):
    password = forms.CharField(
        widget=forms.PasswordInput(),
        label='کلمه عبور',
        validators=[
            validators.MaxLengthValidator(100)
        ]
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(),
        label='تکرار کلمه عبور',
        validators=[
            validators.MaxLengthValidator(100)
        ]
    )



