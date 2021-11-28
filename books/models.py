from django.db import models


class Book(models.Model):
    """Um livro para ser cadastrado"""
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    co_author = models.CharField(max_length=50, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    lent = models.BooleanField(default=False)
    
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