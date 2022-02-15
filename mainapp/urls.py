from django.urls import path
from . import views

app_name = 'mainapp'

urlpatterns = [
    path('', views.products, name='all'),  # 'products'),
    path('<int:pk>', views.category, name='category'),
    # path('/', mainapp.products, name='products'),
    # path('/<int:pk>', mainapp.category, name='category'),
]
# originally without slash
