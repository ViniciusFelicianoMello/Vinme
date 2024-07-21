from django import forms
from allauth.account.forms import SignupForm
from django.contrib.auth.models import User    
from allauth.account.forms import ChangePasswordForm
from django.utils.translation import gettext as _
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)
    profile_picture = forms.ImageField(required=False)

    class Meta:
        model = UserProfile
        fields = ['profile_picture', 'first_name', 'last_name', 'birth_date', 'nationality', 'phone_number', 'biography']

class CustomPasswordChangeForm(ChangePasswordForm):
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(_("As senhas estão diferentes."))
        return password2
    
    def clean_oldpassword(self):
        oldpassword = self.cleaned_data.get('oldpassword')
        if not self.user.check_password(oldpassword):
            raise forms.ValidationError(_("Sua senha atual está incorreta."))
        return oldpassword
    
    
class CustomSignupForm(SignupForm):
    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Este nome de usuário já está em uso. Por favor, escolha outro.")
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este email já está registrado. Por favor, use outro email.")
        return email

class UsernameChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']

    def __init__(self, *args, **kwargs):
        super(UsernameChangeForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
        })
