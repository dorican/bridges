from django.urls import path

from .views import *

app_name = 'authapp'

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/<int:pk>/', UserProfileView.as_view(), name='profile'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    # изменение пароля
    path('profile/password_change/', UserChangePasswordView.as_view(), name='password_change'),
    path('profile/password_change_done/', UserChangePasswordDoneView.as_view(), name='password_change_done'),
    # сброс пароля
    path('profile/password_reset/', UserResetPasswordView.as_view(), name='password_reset'),
    path('profile/password_reset/sent_mail/', UserResetPasswordSentMailView.as_view(), name='password_reset_sent_mail'),
    path('profile/password_reset/<uidb64>/<token>/', UserResetPasswordConfirmView.as_view(), name='password_reset_confirm'),
    path('profile/password_reset/complete/', UserResetPasswordCompleteView.as_view(), name='password_reset_complete'),
]
