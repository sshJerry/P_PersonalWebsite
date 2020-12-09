from django import forms
from .models import CCSUMajors
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import password_validation
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.validators import UnicodeUsernameValidator

username_validator = UnicodeUsernameValidator()


class ProjectForm(forms.ModelForm):
    class Meta:
        model = CCSUMajors
        fields = '__all__'


class SignUpForm(UserCreationForm):
    styleTag = 'flex-grow: 1; box-sizing: border-box; font-size: 1rem; font-weight: 300; display: block; margin: 0; ' \
               'border: none; padding: 0.5em 0; line-height: 1; transition: border-color 0.2s;'
    username = forms.CharField(
        max_length=20,
        min_length=3,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={'unique': _("A user with that username already exists.")},
        widget=forms.TextInput(attrs={'placeholder': 'Username', 'style': styleTag}),
    )
    password1 = forms.CharField(
        max_length=20,
        min_length=3,
        widget=(forms.PasswordInput(attrs={'placeholder': 'Password', 'style': styleTag})),
        help_text=password_validation.password_validators_help_text_html())
    password2 = forms.CharField(max_length=20, min_length=3,
                                widget=forms.PasswordInput(
                                    attrs={'placeholder': 'Password Confirmation', 'style': styleTag}),
                                help_text=_('Just Enter the same password, for confirmation'))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
