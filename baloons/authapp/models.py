from django.db import models
from django.contrib.auth.models import AbstractUser


class ShopUser(AbstractUser):
    avatar = models.ImageField(upload_to='users_avatars', blank=True)
    age = models.PositiveIntegerField(verbose_name='возраст', blank=True)

    def delete(self, using=None, keep_parents=False):
        self.is_active = False
        self.save()


