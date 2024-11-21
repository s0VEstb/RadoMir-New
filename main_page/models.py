from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='books', null=True, blank=True)
    description = models.TextField(max_length=500)
    price = models.IntegerField()
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE)
    author_gmail = models.EmailField()
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.title


    @property
    def average_rating(self):
        last_five_comments = self.comments.order_by('-created_at')[:5]
        average = last_five_comments.aggregate(models.Avg('rate'))['rate__avg']
        return round(average, 2) if average is not None else "Нет оценок"


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


RATE_LIST = [(i, str(i)) for i in range(1, 6)]
class Comment(models.Model):
    text = models.TextField(max_length=500)
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name='comments')
    rate = models.IntegerField(choices=RATE_LIST, default=1, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.book.title