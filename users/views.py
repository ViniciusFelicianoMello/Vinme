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