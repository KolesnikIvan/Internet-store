from django.shortcuts import render

MENU_LINKS = [
    {'url': 'main', 'name': 'в дом'}, 
    {'url': 'products', 'name': 'в продукты'}, 
    {'url': 'contact', 'name': 'в контакты'}
]

RIBBON_MENU = [
    'всё', 'домой', 'офисно', 'модерново', 'классик',
]

# Create your views here.
def main(request):
    return render(request, 'mainapp/index.html',  context ={
        'title': 'Главная',
        'menu_links': MENU_LINKS,
    })


def products(request):
    SIMILAR_PRODUCTS = [
        {'description': 'зеброяйцо', 'destination':'Люстра', 'pic': 'product-11.jpg'},
        {'description': 'икееподобный', 'destination':'Стул', 'pic': 'product-21.jpg'},
        {'description': 'гнутая стойка', 'destination':'Торшер', 'pic':'product-31.jpg'},
    ]
    three_pics = [
        {'adr': 'controll.jpg',},
        {'adr': 'controll1.jpg',},
        {'adr': 'controll2.jpg',},
    ]
    return render(request, 'mainapp/products.html',  context ={
        'title': 'Продукты',
        'menu_links': MENU_LINKS,
        'sim_products': SIMILAR_PRODUCTS, 
        'pics': three_pics,
        'ribbon_menu': RIBBON_MENU,
    })


def contact(request):
    return render(request, 'mainapp/contact.html',  context ={
        'title': 'Контакты',
        'menu_links': MENU_LINKS,
    })
