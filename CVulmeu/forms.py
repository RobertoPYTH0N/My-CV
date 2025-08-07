from django import forms
from .models import Mesaj

class FormularMesaj(forms.ModelForm):
    class Meta:
        model = Mesaj
        fields = ['email', 'mesaj']
        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'mesaj': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Message', 'cols':"40", 'rows':"5"})}