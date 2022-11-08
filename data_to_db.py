import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_test_site.settings')

application = get_wsgi_application()

from cms.models import CmsSlider
from telebot.models import TeleSettings
from price.models import PriceCard, PriceTable

slider_data = {
    'data_1': {
        'img': 'sliderimg/1.jpg',
        'title': 'Первый слайд',
        'text': 'Первый тестовый текст',
        'css': 'active',
    },
    'data_2': {
        'img': 'sliderimg/2.jpg',
        'title': 'Второй слайд',
        'text': 'Второй тестовый текст',
        'css': '-',
    },
    'data_3': {
        'img': 'sliderimg/3.jpg',
        'title': 'Третий слайд',
        'text': 'Третий тестовый текст',
        'css': '-',
    },
    'data_4': {
        'img': 'sliderimg/4.jpg',
        'title': 'Четвертый слайд',
        'text': 'Четвертый тестовый текст',
        'css': '-',
    },
    'data_5': {
        'img': 'sliderimg/5.jpg',
        'title': 'Пятый слайд',
        'text': 'Пятый тестовый текст',
        'css': '-',
    }
}
chat_bot_data = {
    'token': '5590193388:AAHGbcuxBemr8MBHDhUTeYBnL7AdjNEjKVI',
    'chat_id': '-867564951',
    'message': 'Заявка с сайта: Имя: { name } Телефон: { phone }'
}
price_card_data = {
    'card_1': {
        'price': 1000,
        'description': 'Цена №1',
    },
    'card_2': {
        'price': 2000,
        'description': 'Цена №2',
    },
    'card_3': {
        'price': 3000,
        'description': 'Цена №3',
    },
}
price_table_data = {
    'table_1': {
        'title': 'Услуга №1',
        'old_price': 1000,
        'new_price': 500,
    },
    'table_2': {
        'title': 'Услуга №2',
        'old_price': 2000,
        'new_price': 1000,
    },
    'table_3': {
        'title': 'Услуга №3',
        'old_price': 3000,
        'new_price': 1500,
    },
}

bot_data_to_db = TeleSettings(tg_token=chat_bot_data['token'],
                              tg_chat=chat_bot_data['chat_id'],
                              tg_message=chat_bot_data['message']
                              )

bot_data_to_db.save()

for data in slider_data.values():
    save_data = CmsSlider(cms_img=data['img'],
                          cms_title=data['title'],
                          cms_text=data['text'],
                          cms_css=data['css']
                          )
    save_data.save()

for card in price_card_data.values():
    save_card_data = PriceCard(pc_value=card['price'],
                               pc_description=card['description'],
                               )
    save_card_data.save()

for table in price_table_data.values():
    save_table_data = PriceTable(pc_title=table['title'],
                                 pc_old_price=table['old_price'],
                                 pc_new_price=table['new_price'],
                                 )
    save_table_data.save()

print('Test data is written to the database, you can change it in the admin panel!')
