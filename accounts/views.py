from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login
from .models import Userprofile



def vendor_detail(request, pk):
    user = User.objects.get(id=pk)
    context = {
        'user': user
    }
    return render(request, 'accounts/vendor-detail.html', context=context)

def myaccount(request):
    return render(request, 'accounts/myaccount.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            userprofile = Userprofile.objects.create(user=user)
            return redirect('main:home-page')
    else:
        form = UserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/sign-up.html', context=context)
