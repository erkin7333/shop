from django.urls import path
from . views import (homepage, aboutpage, product_detail, category_detail, search,
                     add_to_cart, view_cart, delet_cart, change_quantity)


app_name = "main"


urlpatterns = [
    path('', homepage, name='home-page'),

    path('about/', aboutpage, name='about-page'),

    path('product_detail/<slug:slug>/', product_detail, name='product_detail'),

    path('category-detail<slug:slug>/', category_detail, name='category_detail'),

    path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),

    path('cart/', view_cart, name='cart_view'),

    path('change-quantity/<str:product_id>/', change_quantity, name='change_quantity'),

    path('delet-cart/<int:product_id>/', delet_cart, name='delet_cart'),

    path('search/', search, name='search')
]