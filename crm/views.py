from django.shortcuts import render

from cms.models import CmsSlider
from crm.forms import OrderForm
from crm.models import Order
from price.models import PriceCard, PriceTable
from telebot.send_message import send_telegram


def first_page(request):
    slider_list = CmsSlider.objects.all()
    card_list = PriceCard.objects.all().order_by('id')[:3]
    pc_1 = card_list[0]
    pc_2 = card_list[1]
    pc_3 = card_list[2]
    price_table = PriceTable.objects.all()
    form = OrderForm()
    dict_obj = {
        'slider_list': slider_list,
        'pc_1': pc_1,
        'pc_2': pc_2,
        'pc_3': pc_3,
        'prise_table': price_table,
        'form': form,
    }
    return render(request, 'index.html', dict_obj)


def thanks_page(request):
    if request.POST:
        name = request.POST['name']
        phone = request.POST['phone']
        order_to_save = Order(order_name=name, order_phone=phone)
        order_to_save.save()
        send_telegram(tg_name=name, tg_phone=phone)
        return render(request, 'thanks.html', {'name': name})
    else:
        return render(request, 'thanks.html')
