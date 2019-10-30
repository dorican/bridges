from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm

from .models import Users


class RegisterUserForm(ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Введите логин*'}),
                               min_length=5, max_length=15)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'придумайте пароль*'}),
                               min_length=5, max_length=15)
    phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'и укажите телефон для связи*'}),
                            min_length=16, max_length=16)

    class Meta:
        model = Users
        RegisterUserFormFields = ('username', 'password', 'phone')
        exclude = ['date_joined']

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        user.is_active = False
        if commit:
            user.save()
        return user


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Введите логин*'}),
                               min_length=5, max_length=15)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'и пароль*'}),
                               min_length=8, max_length=15)

    class Meta:
        model = Users
        AuthenticationFormFields = ('username', 'password')


class UserChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Введите старый пароль*'}),
                                   min_length=8, max_length=15)
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Придумайте новый пароль*'}),
                                    min_length=8, max_length=15)
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'и повторите новый пароль*'}),
                                    min_length=8, max_length=15)

    class Meta:
        model = Users
        UserChangePasswordFormFields = ('old_password', 'new_password1', 'new_password2')


class UserResetPasswordForm(PasswordResetForm):
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Введите электронную почту*'}))

    class Meta:
        model = Users
        AuthenticationFormFields = ('email',)


class UserSetNewPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Придумайте новый пароль*'}),
                                    min_length=8, max_length=15)
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'и повторите новый пароль*'}),
                                    min_length=8, max_length=15)

    class Meta:
        model = Users
        UserSetNewPasswordFormFields = ('new_password1', 'new_password2')
