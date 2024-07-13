from django import forms
from .models import ContactMessage

class contactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'subject': forms.Select(choices=ContactMessage.subjectChoises)
        }