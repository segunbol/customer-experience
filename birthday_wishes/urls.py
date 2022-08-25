from django.urls import path
from . import views

app_name = 'birthday_wishes'

urlpatterns = [
    path('', views.list_of_customers, name='list_of_customers'),
    path('customer/<slug:slug>/' , views.customer_page, name='customer_page'),
]