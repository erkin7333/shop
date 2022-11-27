from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
from django.contrib import messages
from .models import Userprofile
from .forms import ProductForm
from main.models import Product, Category


def vendor_detail(request, pk):
    user = User.objects.get(id=pk)
    context = {
        'user': user
    }
    return render(request, 'accounts/vendor-detail.html', context=context)

@login_required
def myaccount(request):
    return render(request, 'accounts/myaccount.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            userprofile = Userprofile.objects.create(user=user)
            return redirect('accounts:login')
    else:
        form = UserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/sign-up.html', context=context)

@login_required
def my_stor(request):

    return render(request, 'accounts/my-store.html')

@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            title = request.POST.get('title')
            product = form.save(commit=False)
            product.user = request.user
            product.slug = slugify(title)
            product.save()
            messages.success(request, "Maxsulot qo'shildi")
            return redirect('accounts:my_stor')
    else:
        form = ProductForm()
    context = {
        'title': "Maxsulot qo'shish",
        'form': form
    }
    return render(request, 'accounts/add-product.html', context=context)


@login_required
def edit_product(request, pk):
    product = Product.objects.filter(user=request.user).get(id=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "Maxsulot o'zgartirildi")
            return redirect('accounts:my_stor')
    else:
        form = ProductForm(instance=product)
    context = {
        'title': "Maxsulotni o'zgartirish",
        'form': form
    }
    return render(request, 'accounts/add-product.html', context=context)


@login_required
def delete_product(request, pk):
    product = Product.objects.filter(user=request.user).get(id=pk)

