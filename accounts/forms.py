from django import forms
from main.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('category', 'title', 'description', 'price', 'image',)
        widgets = {
            'category': forms.Select(attrs={
                'class': 'w-full p-4 border border-gray-500'
            }),
            'title': forms.TextInput(attrs={
                'class': 'w-full p-4 border border-gray-500'
            }),
            'description': forms.Textarea(attrs={
                'class': 'w-full p-4 border border-gray-500'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'w-full p-4 border border-gray-500'
            }),
            'image': forms.FileInput(attrs={
                'class': 'w-full p-4 border border-gray-500'
            })
        }