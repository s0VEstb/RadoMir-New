from django.db import models
from main_page.models import Book


class Order(models.Model):
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='orders')

    def __str__(self):
        return f"{self.name} - {self.book.title}"

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
