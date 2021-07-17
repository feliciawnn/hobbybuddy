from django.contrib.auth.forms import UsernameField, AuthenticationForm
from django.contrib.auth import password_validation
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _


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