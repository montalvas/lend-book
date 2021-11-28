from django.db import models

class User(models.Model):
    """Dados do usuário"""
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=64)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
