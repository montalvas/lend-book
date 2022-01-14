from django.db import models
from users.models import User
from stdimage.models import StdImageField


class Category(models.Model):
    """Categoria para cada livro"""
    name = models.CharField(max_length=30)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    
    class Meta:
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name

class Book(models.Model):
    """Um livro para ser cadastrado"""
    image = StdImageField(upload_to='book_cover', blank=True, null=True)
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    co_author = models.CharField(max_length=50, blank=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    date_added = models.DateTimeField(auto_now_add=True)
    lent = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    
    def __str__(self):
        """Nome do livro"""
        if len(self.name) > 20:
            return self.name[:20] + "..."
        else:
            return self.name

class Loan(models.Model):
    """Empréstimo do livro"""
    borrower = models.CharField(max_length=50)
    loan_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    
    def __str__(self):
        """Nome do mutuário"""
        return self.borrower