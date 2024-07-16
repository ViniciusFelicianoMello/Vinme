from django.urls import path
from users.views import CustomPasswordChangeView, complete_profile, profile_view
from . import views

urlpatterns = [
    path('password/change/', CustomPasswordChangeView.as_view(), name='account_change_password'),
    path('complete-profile/', complete_profile, name='complete_profile'),
    path('profile/', profile_view, name='profile_view'),
]