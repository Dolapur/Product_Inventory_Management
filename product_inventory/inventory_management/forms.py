from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    name = forms.CharField(max_length=150, widget=forms.TextInput(attrs={
        'class': "form-control me-2", 'placeholder': 'Product name'
    }))
    description = forms.CharField(widget=forms.Textarea(attrs={
        'class': "form-control me-2", 'placeholder': 'Product description'
    }))
    price = forms.DecimalField(max_digits=10, decimal_places=2, widget=forms.NumberInput(attrs={
        'class': "form-control me-2", 'placeholder': 'Price'
    }))
    
    class Meta:
        model = Product
        fields = '__all__'