import random
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

def get_hot_product(queryset):  #request, pk):
    # return random.choice(Product.objects.all())
    return random.choice(queryset)

def products(request):
    categories = ProductCategory.objects.all()
    products = Product.objects.all()  # [:4]
    hot_product = get_hot_product(products)
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
        'products': products.exclude(pk=hot_product.pk),  # [:4]
        'hot_product': hot_product,
    })


def category(request, category_id):
    # return products(request)
    # category = ProductCategory.objects().get(pk=pk)  # current category
    categories = ProductCategory.objects.all()       # all categories
    category = get_object_or_404(ProductCategory, pk=category_id)
    products = Product.objects.filter(category=category)
    hot_product = get_hot_product(products)
    return render(
        request,
        "mainapp/products.html",
        context={
            "title": 'Prods', 
            "products": products.exclude(pk=hot_product.pk),  # [:4]
            "menu_links": MENU_LINKS,
            "categories": categories,
            'hot_product': hot_product,  # get_hot_product(products),
        },
    )


def product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    categories = ProductCategory.objects.all()
    
    return render(
        request,
        'mainapp/product.html',
        context={
            'title': product.name,
            'product': product,
            'menu_links': MENU_LINKS,
            'categories': categories,
        }
    )
    return render(request, 'mainapp/product.html', context={
        'pk':pk,
    })


def contact(request):
    return render(request, 'mainapp/contact.html',  context ={
        'title': 'Контакты',
        'menu_links': MENU_LINKS,
    })
