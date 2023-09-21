from django import forms
from .models import Product

# This will be instantiated in views
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]