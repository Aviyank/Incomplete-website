from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(requset):
    return render(requset, 'accounts/dashboard.html')

def products(requset):
    return render(requset, 'accounts/products.html')

def customer(requset):
    return render(requset, 'accounts/customer.html')
