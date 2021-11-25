from django.db import models


class Books(models.Model):
    """Um livro para ser cadastrado"""
    name = models.CharField(max_length = 100)
    author = models.CharField(max_length = 50)
    co-author = models.CharField(max_length = 50)
    date_register = models.DateTimeField(auto_now_add=True)
    lent = models.BooleanField(default=False)
    