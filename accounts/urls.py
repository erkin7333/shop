from django.urls import path
from .views import vendor_detail, signup, myaccount
from django.contrib.auth import views as auth_views

app_name = "accounts"

urlpatterns = [
    path('signup/', signup, name='sign_up'),

    path('myaccount/', myaccount, name='myaccount'),

    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),

    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('vendor-detail/<int:pk>/', vendor_detail, name='vendor_detail')
]