from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from django.contrib.auth.models import User
from django.db.models import Q



def homepage(request):
    product = Product.objects.all()[0:6]
    context = {
        'product': product
    }
    return render(request, "main/home.html", context=context)


def aboutpage(request):
    return render(request, "main/about.html")

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    context = {
        'product': product
    }
    return render(request, 'product/product-detail.html', context=context)

def category_detail(request, slug):
    categories = get_object_or_404(Category, slug=slug)
    product = categories.products.all()
    context = {
        'categories': categories,
        'product': product
    }
    return render(request, 'product/category-detail.html', context=context)


def search(request):
    query = request.GET.get('query', '')
    products = Product.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))

    context = {
        'query': query,
        'products': products
    }
    return render(request, 'product/search.html', context=context)
