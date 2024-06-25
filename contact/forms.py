# forms.py
from django import forms

from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'apellido', 'email', 'phone', 'message']
    
    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if not phone.isdigit():
            raise forms.ValidationError("El número de teléfono debe contener solo dígitos.")
        return phone