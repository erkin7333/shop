from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category
from django.contrib.auth.models import User
from django.db.models import Q
from .cart import Cart


def homepage(request):
    product = Product.objects.filter(status=Product.ACTIVE)[0:6]
    context = {
        'product': product
    }
    return render(request, "main/home.html", context=context)


def aboutpage(request):
    return render(request, "main/about.html")

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, status=Product.ACTIVE)
    cart = Cart(request)
    print("JAmi summaaa===========-------------..>>>>>>", cart.get_total_cost())
    context = {
        'product': product
    }
    return render(request, 'product/product-detail.html', context=context)

def category_detail(request, slug):
    categories = get_object_or_404(Category, slug=slug)
    product = categories.products.filter(status=Product.ACTIVE)
    context = {
        'categories': categories,
        'product': product
    }
    return render(request, 'product/category-detail.html', context=context)


def search(request):
    query = request.GET.get('query', '')
    products = Product.objects.filter(status=Product.ACTIVE).filter(Q(title__icontains=query) | Q(description__icontains=query))

    context = {
        'query': query,
        'products': products
    }
    return render(request, 'product/search.html', context=context)


def add_to_cart(request, product_id):
    cart = Cart(request)
    cart.add(product_id)
    return redirect('main:cart_view')

def view_cart(request):
    cart = Cart(request)
    context = {
        'cart': cart
    }
    return render(request, 'product/cart.html', context=context)

def change_quantity(request, product_id):
    action = request.GET.get('action', '')
    if action:
        quantity = 1
        if action == 'decrease':
            quantity = -1
        cart = Cart(request)
        cart.add(product_id, quantity, True)
    return redirect('main:cart_view')





def delet_cart(request, product_id):
    cart = Cart(request)
    cart.remove(str(product_id))

    return redirect('main:cart_view')