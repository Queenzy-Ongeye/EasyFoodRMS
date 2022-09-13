from django import forms
from django.forms import ModelForm
from .models import Shop

# Create a shop form
class ShopForm(ModelForm):
    class Meta:
        model = Shop
        fields = ('name','tagline', 'image')