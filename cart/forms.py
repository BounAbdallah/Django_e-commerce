import imaplib
from django import forms


PRODUCT_QUANTITY_CHOICES =   [(i, str(i)) for i in range(1, 51)]
class CarteAddProductForm(forms.Form):
    quantity= forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int,
    label="Quantité")

    override = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)