from django.shortcuts import render, get_object_or_404
from .models import Customer, Group


def all_customers(request):
    return {
        'all_customers': Customer.objects.all()
    }

def all_groups(request):
    return {
        'all_groups': Group.objects.all()
    }

def list_of_customers(request):
    customers = Customer.objects.all()
    return render(request, 'Birthday/index.html', {'customers':customers})

def customer_page(request, slug):
    customer = get_object_or_404(Customer, slug=slug)
    return render(request, 'Birthday/mobile.html', {'customer':customer})



