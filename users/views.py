from allauth.account.views import PasswordChangeView
from .forms import CustomPasswordChangeForm
from django.contrib import messages
from django.utils.translation import gettext as _

class CustomPasswordChangeView(PasswordChangeView):
    form_class = CustomPasswordChangeForm

    def form_invalid(self, form):
        if 'oldpassword' in form.errors:
            messages.error(self.request, _('Sua senha atual está incorreta.'))
        return super().form_invalid(form)

    def form_valid(self, form):
        messages.success(self.request, _('Senha alterada com sucesso!'))
        return super().form_valid(form)
    

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from users.forms import UserProfileForm
from users.models import UserProfile

@login_required
def complete_profile(request):
    try:
        profile = request.user.userprofile
    except UserProfile.DoesNotExist:
        profile = None
    
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('index')
    else:
        form = UserProfileForm(instance=profile)
    
    return render(request, 'users/complete_profile.html', {'form': form})

@login_required
def profile_view(request):
    try:
        profile = request.user.userprofile
    except UserProfile.DoesNotExist:
        profile = None
    
    return render(request, 'profile.html', {'profile': profile})