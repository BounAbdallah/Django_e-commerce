from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    full_name = forms.CharField(label="Nom complet", widget=forms.TextInput({"class": "form-control", "placeholder": "Votre nom complèt"}))
    address = forms.CharField(label="Addresse de livraison", widget=forms.TextInput({"class": "form-control", "placeholder": "Votre addresse de livraison"}))
    phone = forms.CharField(label="Numéro de téléphone", widget=forms.TextInput({"class": "form-control", "placeholder": "Votre numéro de téléphone"}))
    email = forms.EmailField(label="Mail", widget=forms.EmailInput({"class": "form-control", "placeholder": "Votre addresse mail"}))
    
    class Meta:
        model = Order
        fields = ("full_name","email","phone","address")




