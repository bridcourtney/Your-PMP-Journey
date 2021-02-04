from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.

def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.filter(is_a_service=False)

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)

def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)


def courses(request):
    """ A view to display all of the courses"""
    products = Product.objects.filter(is_a_service=True)
    context = {
        'products': products,
    }

    return render(request, 'products/courses.html', context)


def course_detail(request, product_id):
    """ A view to show individual course details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/course_detail.html', context)