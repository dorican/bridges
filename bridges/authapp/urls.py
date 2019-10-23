from django.urls import path
from .views import *

app_name = 'authapp'

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/<int:pk>/', UserProfileView.as_view(), name='profile'),
    path('profile/password_change/', UserChangePasswordView.as_view(), name='password_change'),
    path('profile/password_change_done/', UserChangePasswordDoneView.as_view(), name='password_change_done'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
]
