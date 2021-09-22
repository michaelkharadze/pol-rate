from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordResetForm, SetPasswordForm, UsernameField
from captcha.fields import CaptchaField

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label = "ელ-ფოსტა")
    username = UsernameField(label="მომხმარებლის სახელი", widget=forms.TextInput(attrs={'autofocus': True}))
    password1 = forms.CharField(widget=forms.PasswordInput(), label="პაროლი")
    password2 = forms.CharField(widget=forms.PasswordInput(), label="გაიმეორეთ პაროლი")
    captcha = CaptchaField(label=" ", error_messages={'invalid': 'არასწორი პასუხი'})

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'captcha']

class CustomAuthenticationForm(AuthenticationForm):
    username = UsernameField(
        label='მომხმარებლის სახელი',
        widget=forms.TextInput(attrs={'autofocus': True})
    )
    password = forms.CharField(label="პაროლი", widget=forms.PasswordInput())
    captcha = CaptchaField(label=" ", error_messages={'invalid': 'არასწორი პასუხი'})

class UserPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label='ელ-ფოსტა')
    captcha = CaptchaField(label=" ")

class UserPasswordSetForm(SetPasswordForm):
    new_password1 = forms.CharField(label="ახალი პაროლი", widget=forms.PasswordInput())
    new_password2 = forms.CharField(label="გაიმეორეთ პაროლი", widget=forms.PasswordInput())