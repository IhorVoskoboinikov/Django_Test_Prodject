from django.shortcuts import render

from crm.models import Order
from crm.forms import OrderForm


# Create your views here.

def first_page(request):
    object_list = Order.objects.all()
    form = OrderForm()
    return render(request, 'main.html', {
        'object_list': object_list,
        'form': form
    })


def form_done(request):
    name = request.POST['name']
    phone = request.POST['phone']
    order_to_save = Order(order_name=name, order_phone=phone)
    order_to_save.save()
    return render(request, 'form_done.html', {
        'name': name,
        'phone': phone
    })
