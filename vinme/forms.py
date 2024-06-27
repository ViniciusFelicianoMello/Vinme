from django import forms
from django.core.validators import EmailValidator 

class contactForm(forms.Form):
    name = forms.CharField(max_length=100, label='Nome')
    email = forms.EmailField(validators=[EmailValidator()], label='Email')
    subject = forms.CharField(max_length=200, label='Assunto')
    message = forms.CharField(widget=forms.Textarea, label='Mensagem') 