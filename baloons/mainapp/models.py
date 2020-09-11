from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(verbose_name='имя', max_length=64, unique=True)
    description = models.TextField(verbose_name='описание', blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='название продукта', max_length=128)
    image = models.ImageField(upload_to='products_images', blank=True)
    color = models.CharField(verbose_name='цвет', max_length=60, blank=True)
    short_desc = models.CharField(verbose_name='краткое описание продукта', max_length=60, blank=True)
    description = models.TextField(verbose_name='описание продукта', blank=True)
    price = models.DecimalField(verbose_name='цена продукта', max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(verbose_name='количество на складе', default=0)
    reference = models.CharField(verbose_name='артикул', max_length=20, blank=False, unique=True)
    shape = models.CharField(verbose_name='форма', max_length=80, blank=True)
    size = models.PositiveSmallIntegerField(verbose_name='размер', blank=True)

    def __str__(self):
        return self.name

