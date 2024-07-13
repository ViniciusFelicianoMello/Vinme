from django.shortcuts import render
from django.contrib.auth.views import PasswordChangeView
from users.forms import ChangePasswordForm

class CustomPasswordChangeView(PasswordChangeView):
    form_class = ChangePasswordForm
    template_name = 'account/password_change.html'
    success_url = 'index'