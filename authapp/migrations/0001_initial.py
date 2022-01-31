# Generated by Django 3.1 on 2022-01-26 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShopUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('age', models.PositiveIntegerField(verbose_name='age')),
                ('avatar', models.ImageField(blank=True, upload_to='users', verbose_name='avatar')),
                ('phone', models.CharField(blank=True, max_length=20, unique=True, verbose_name='telephone')),
                ('city', models.CharField(blank=True, max_length=20, verbose_name='city')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]