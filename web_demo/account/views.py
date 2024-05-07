from django.shortcuts import render, HttpResponse, redirect
from .models import Product

# Create your views here.

def test_view(request):
    return HttpResponse("hello")



def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})
