
from django.shortcuts import render
from . import views
from django.urls import path

app_name = "website"

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('contacts', views.contacts, name='contacts'),
    path('products', views.products, name='products')
]