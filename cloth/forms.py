# cloth/forms.py
from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer', 'products']
        widgets = {
            'products': forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)

