from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView, \
    PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.views.generic.detail import DetailView

from .forms import *
from .models import *


# Create your views here.

class RegisterUserView(CreateView):
    model = Users
    form_class = RegisterUserForm
    extra_context = {
        'page_title': 'Регистрация на сайте',
        'bred_title': 'Регистрация'
    }
    template_name = 'authapp/register.html'
    success_url = reverse_lazy('auth:register_done')

    def form_valid(self, form):
        # проверка валидности reCAPTCHA
        if self.request.recaptcha_is_valid:
            form.save()
            return render(self.request, 'authapp/register_done.html', self.get_context_data())
        return render(self.request, 'authapp/register.html', self.get_context_data())


class RegisterUserDoneView(TemplateView):
    extra_context = {
        'page_title': 'Регистрация на сайте',
        'bred_title': 'Регистрация'
    }
    template_name = 'authapp/register_done.html'


class UserLoginView(LoginView):
    authentication_form = LoginUserForm
    extra_context = {
        'page_title': 'Авторизация на сайте',
        'bred_title': 'Авторизация'
    }
    template_name = 'authapp/login.html'


class UserProfileView(LoginRequiredMixin, DetailView):
    login_url = '/auth/login/'
    redirect_field_name = 'redirect_to'
    model = Users
    extra_context = {
        'page_title': 'Профиль пользователя',
        'bred_title': 'Профиль пользователя'
    }
    template_name = 'authapp/profile.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        return context


class UserChangePasswordView(LoginRequiredMixin, PasswordChangeView):
    login_url = '/auth/login/'
    redirect_field_name = 'redirect_to'
    form_class = UserChangePasswordForm
    extra_context = {
        'page_title': 'Изменение пароля',
        'bred_title': 'Изменение пароля'
    }
    template_name = 'authapp/password_change.html'
    success_url = reverse_lazy('auth:password_change_done')


class UserChangePasswordDoneView(LoginRequiredMixin, PasswordChangeDoneView):
    login_url = '/auth/login/'
    redirect_field_name = 'redirect_to'
    extra_context = {
        'page_title': 'Изменение пароля',
        'bred_title': 'Изменение пароля'
    }
    template_name = 'authapp/password_change_done.html'


class UserResetPasswordView(PasswordResetView):
    form_class = UserResetPasswordForm
    extra_context = {
        'page_title': 'Сброс пароля',
        'bred_title': 'Сброс пароля'
    }
    template_name = 'authapp/password_reset.html'
    email_template_name = 'authapp/reset_email.html'
    success_url = reverse_lazy('auth:password_reset_sent_mail')


class UserResetPasswordSentMailView(PasswordResetDoneView):
    extra_context = {
        'page_title': 'Сброс пароля',
        'bred_title': 'Сброс пароля'
    }
    template_name = 'authapp/password_reset_sent_mail.html'


class UserResetPasswordConfirmView(PasswordResetConfirmView):
    form_class = UserSetNewPasswordForm
    extra_context = {
        'page_title': 'Установка нового пароля',
        'bred_title': 'Установка пароля'
    }
    template_name = 'authapp/password_reset_confirm.html'
    success_url = reverse_lazy('auth:password_reset_complete')


class UserResetPasswordCompleteView(PasswordResetCompleteView):
    extra_context = {
        'page_title': 'Установка нового пароля',
        'bred_title': 'Установка пароля'
    }
    template_name = 'authapp/password_reset_complete.html'


class UserLogoutView(LogoutView):
    extra_context = {
        'page_title': 'Выход с сайта',
        'bred_title': 'Выход с сайта'
    }
    template_name = 'authapp/logout.html'
