from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import AbstractUser, BaseUserManager

# class UserManager(BaseUserManager):
#     hello = 'hello world!'
    # def create_superuser(self,)


# Create your models here.
# class ShopUser(AbstractBaseUser):  # models.Model):
class ShopUser(AbstractUser):  # models.Model):
    # наследуем абстрактного, чтоб не создавать поля, обязательные для модели
    # REQUIRED_FIELDS = ('age',)
    # USERNAME_FIELD = 'phone'
    username = models.CharField(verbose_name='name', default='default user', unique=True, max_length=20)
    age = models.PositiveIntegerField(verbose_name='age')
    avatar = models.ImageField(verbose_name='avatar', blank=True, upload_to='users')
    phone = models.CharField(verbose_name='telephone', max_length=20, blank=True)  # , unique=True)
    city = models.CharField(verbose_name='city', max_length=20, blank=True)

    # objects = BaseUserManager()  # добавил, потому что fill_db не работал
