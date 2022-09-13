from django.shortcuts import render
from .models import Shop

# Create your views here.

def home(request):
    all_shops = Shop.objects.all()
    return render(request, 'shops/home.html', {'shops' : all_shops}) 