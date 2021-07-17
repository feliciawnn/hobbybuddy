from django.contrib.auth.forms import UserCreationForm, UsernameField, AuthenticationForm
from django.contrib.auth import password_validation
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _


class SignUpForm(UserCreationForm):
    email = forms.CharField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    username = UsernameField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'placeholder': 'Password'}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'placeholder': 'Password Confirmation'}),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]


class SignInForm(AuthenticationForm):
    username = UsernameField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'placeholder': 'Password'}),
        help_text=password_validation.password_validators_help_text_html(),

    )

    class Meta:
        model = User
        fields = ["username", "password"]
