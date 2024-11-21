from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Тег')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Cloth(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    image = models.ImageField(upload_to='clothes', verbose_name='Cloth', null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    tags = models.ManyToManyField(Tag, related_name='clothes', verbose_name='Теги')

    def __str__(self):
        return f"{self.title} - {self.tags.name}"

