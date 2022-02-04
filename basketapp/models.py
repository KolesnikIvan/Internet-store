from django.db import models
from django.conf import settings
from mainapp.models import Product

# Create your models here.
class Basket(models.Model):
    class Meta:
        ordering = ('-quantity',)
        unique_together = ['user', 'product']
        
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, unique=True, on_delete=models.CASCADE, related_name='basket')
    # product = models.ForeignKey(Product, unique=True, on_delete=models.CASCADE)
    # user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='basket')
    # product = models.OneToOneField(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='basket')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='quantity of goods', default=0)
    add_datetime = models.DateTimeField(verbose_name='time', auto_now_add=True)

    def __str__(self):
        return f'{self.product.name} - {self.quantity} pieces.'
