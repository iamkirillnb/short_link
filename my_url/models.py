from random import randint, choice
from django.utils.crypto import get_random_string
from django.db import models

def change_url():
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    url_add = ''
    for i in range(randint(5, 15)):
        url_add += choice(letters)
    return url_add


class Links(models.Model):
    link = models.URLField(max_length=100, blank=False, unique=True, verbose_name='link')
    shortened = models.CharField(max_length=50, default=lambda: change_url(), unique=True, verbose_name='short_link')
    change_flag = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'link'
        verbose_name_plural = 'links'

    def __str__(self):
        return self.link

