from django.contrib import admin
from django.shortcuts import render
from django.urls import path
from . import views

from products.models import Product, ProductReview

# Create your views here.

def index(request):
    """ A view to return the index page """
    
    reviews = ProductReview.objects.all()

    context = {
        'reviews': reviews,
    }
    
    return render(request, 'home/index.html', context)