from allauth.account.views import PasswordChangeView
from .forms import CustomPasswordChangeForm
from django.contrib import messages
from django.utils.translation import gettext as _


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from users.forms import UserProfileForm
from users.models import UserProfile
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404

from vinme.views import pages, add_pages_context

class CustomPasswordChangeView(PasswordChangeView):
    form_class = CustomPasswordChangeForm

    def form_invalid(self, form):
        if 'oldpassword' in form.errors:
            messages.error(self.request, _('Sua senha atual está incorreta.'))
        return super().form_invalid(form)

    def form_valid(self, form):
        messages.success(self.request, _('Senha alterada com sucesso!'))
        return super().form_valid(form)
    


@login_required
def complete_profile(request):
    user = request.user
    user_profile, created = UserProfile.objects.get_or_create(user=user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            print("Form saved successfully")
            return redirect('profile_view', username=user.username)
        else:
            print("Form is not valid", form.errors)
    else:
        form = UserProfileForm(instance=user_profile)
    
    return render(request, 'users/complete_profile.html', {'form': form})

@login_required
def profile_view(request, username):
    user = get_object_or_404(User, username=username)
    try:
        profile = user.userprofile
    except UserProfile.DoesNotExist:
        profile = None
    
    context = {'profile': profile}
    context = add_pages_context(context) 
    return render(request, 'users/profile.html', context)