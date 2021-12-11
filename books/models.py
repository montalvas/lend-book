from django.db import models
from users.models import User


class Category(models.Model):
    """Categoria para cada livro"""
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField()
    
    class Meta:
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name

class Book(models.Model):
    """Um livro para ser cadastrado"""
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    co_author = models.CharField(max_length=50, blank=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    date_added = models.DateTimeField(auto_now_add=True)
    lent = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    
    def __str__(self):
        """Nome do livro"""
        return self.name

class Loan(models.Model):
    """Empréstimo do livro"""
    borrower = models.CharField(max_length=50)
    loan_date = models.DateField()
    borrowed_days = models.IntegerField(default=0)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    
    def __str__(self):
        """Nome do mutuário"""
        return self.borrower