from re import A
from django.shortcuts import render, get_object_or_404
from .models import Customer, Group
from datetime import datetime

gun = []
celebrant = []
customers = Customer.objects.all()
shoot = 0
for customer in customers:
    if shoot<= 1:
        gun.append(customer.date_of_birth)
    shoot = shoot + 1
    if type(customer.date_of_birth) != type(gun[0]):
        pass
    else:
        if customer.date_of_birth.strftime("%m-%d") == datetime.now().strftime('%m-%d'):
            celebrant.append(customer)

def all_customers(request):
    return {
        'all_customers': celebrant
    }

def all_groups(request):
    return {
        'all_groups': Group.objects.all()
    }

def list_of_customers(request):
    customers = Customer.objects.all()
    dated = datetime.now().strftime('%m-%d')
    for customer in customers:
        if customer.date_of_birth.strftime("%m-%d") == dated:
            gun.append(customer.name)
        else:
            pass
    print(gun)
    return render(request, 'Birthday/index.html', {'customers':celebrant})

def customer_page(request, slug):
    customer = get_object_or_404(Customer, slug=slug)
    dated = datetime.now().strftime('%m-%d')
    data = {'customer':customer, 'dated':dated}
    if customer.date_of_birth.strftime("%m-%d") == dated:
        return render(request, 'Birthday/mobile.html', data)
    else:
        return render(request, 'Birthday/notbirthday.html', data)
    
    



