from django.urls import path
from users.views import CustomPasswordChangeView, complete_profile, profile_view, settings_view, change_username
from . import views

urlpatterns = [
    path('password/change/', CustomPasswordChangeView.as_view(), name='account_change_password'),
    path('complete-profile/', complete_profile, name='complete_profile'),
    path('profile/<str:username>/', profile_view, name='profile_view'),
    path('settings/', settings_view, name='settings_view'),
    path('change-username/', change_username, name='change_username'),
    ]