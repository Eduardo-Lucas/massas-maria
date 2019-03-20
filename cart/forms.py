from django import forms

from choices.models import PRODUCT_QUANTITY_CHOICES, DESCONTO_CHOICES


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(label='Quantidade', choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
    # desconto = forms.TypedChoiceField(choices=DESCONTO_CHOICES, coerce=int, required=False)
    # preco_negociado = forms.DecimalField(label='Preço Líquido', decimal_places=2, required=False, initial=True)

