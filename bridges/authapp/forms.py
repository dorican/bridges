from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm

from .models import Users


class RegisterUserForm(ModelForm):
    class Meta:
        model = Users
        fields = ('username', 'password', 'phone')
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Введите логин*'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'придумайте пароль*'}),
            'phone': forms.TextInput(attrs={'placeholder': 'и укажите телефон для связи*', }),
        }

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        user.is_active = False
        if commit:
            user.save()
        return user


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Введите логин*'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'и пароль*'}))

    class Meta:
        model = Users
        AuthenticationFormFields = ('username', 'password')
        exclude = []


class UserChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Введите старый пароль*'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Придумайте новый пароль*'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'и повторите новый пароль*'}))

    class Meta:
        model = Users
        UserChangePasswordFormFields = ('old_password', 'new_password1', 'new_password2')
        exclude = []


class UserResetPasswordForm(PasswordResetForm):
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Введите электронную почту*'}))

    class Meta:
        model = Users
        AuthenticationFormFields = ('email',)
        exclude = []


class UserSetNewPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Придумайте новый пароль*'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'и повторите новый пароль*'}))

    class Meta:
        model = Users
        UserSetNewPasswordFormFields = ('new_password1', 'new_password2')
        exclude = []
