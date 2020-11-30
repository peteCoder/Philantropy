from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):

	class Meta:
		model = Contact
		fields = ['name', 'email', 'phone', 'message']
		widgets = {
			'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Name'}),
			'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder':'Email'}),
			'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Phone'}),
			'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Message Us..'}),
		}
