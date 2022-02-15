from django.shortcuts import render, get_object_or_404
from .models import Product, ProductCategory

MENU_LINKS = [
    {'url': 'main', 'active':['main'], 'name': 'в дом'}, 
    {'url': 'products:all', 'active':['products:all', 'products:category'], 'name': 'в продукты'}, 
    {'url': 'contact', 'active':['contact'], 'name': 'в контакты'}
]

RIBBON_MENU = [
    'всё', 'домой', 'офисно', 'модерново', 'классик',
]

# Create your views here.
def main(request):
    products = Product.objects.all()[:4]
    return render(request, 'mainapp/index.html',  context ={
        'title': 'Главная',
        'menu_links': MENU_LINKS,
        'products': products,
    })


def products(request):
    categories = ProductCategory.objects.all()
    products = Product.objects.all()[:4]
    # SIMILAR_PRODUCTS = [
    #     {'description': 'зеброяйцо', 'destination':'Люстра', 'pic': 'product-11.jpg'},
    #     {'description': 'икееподобный', 'destination':'Стул', 'pic': 'product-21.jpg'},
    #     {'description': 'гнутая стойка', 'destination':'Торшер', 'pic':'product-31.jpg'},
    # ]
    three_pics = [
        {'adr': 'controll.jpg',},
        {'adr': 'controll1.jpg',},
        {'adr': 'controll2.jpg',},
    ]
    return render(request, 'mainapp/products.html',  context ={
        'title': 'Продукты',
        'menu_links': MENU_LINKS,
        # 'sim_products': SIMILAR_PRODUCTS, 
        'pics': three_pics,
        'ribbon_menu': RIBBON_MENU,
        'categories': categories,
        'products': products,
    })


def category(request, pk):
    # return products(request)
    # category = ProductCategory.objects().get(pk=pk)  # current category
    categories = ProductCategory.objects.all()       # all categories
    category = get_object_or_404(ProductCategory, pk=pk)
    products = Product.objects.filter(category=category)
    return render(
        request,
        "mainapp/products.html",
        context={
            "title":'Prods', 
            "products":products,
            "menu_links": MENU_LINKS,
            "categories":categories,
        },
    )

def contact(request):
    return render(request, 'mainapp/contact.html',  context ={
        'title': 'Контакты',
        'menu_links': MENU_LINKS,
    })
