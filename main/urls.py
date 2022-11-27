from django.urls import path
from . views import (homepage, aboutpage, product_detail, category_detail)


app_name = "main"


urlpatterns = [
    path('', homepage, name='home-page'),

    path('about/', aboutpage, name='about-page'),

    path('product_detail/<slug:slug>/', product_detail, name='product_detail'),

    path('category-detail<slug:slug>/', category_detail, name='category_detail'),

]