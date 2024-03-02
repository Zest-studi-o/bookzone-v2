from django.db import models
#from django.contrib.auth.models import User
from checkout.models import Order
from books.models import Book
from django.core.validators import MinValueValidator, MaxValueValidator
import bleach
#to import the custom user
from django.conf import settings

STATUS = ((0, "Draft"), (1, "Published"))

class Review(models.Model):
    review_title = models.CharField(max_length=200, unique=True)
    book_reviewed = models.ForeignKey(Book, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    reviewer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=0)
    content = models.TextField()
    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='order', unique=True) 
    rating = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        #return f'Review by {self.user.username} for {self.book.title}'
        return f'Review by {self.reviewer.username} for {self.book.review_title}'

    def save(self, *args, **kwargs):
        self.content = bleach.clean(self.content, tags=[], attributes={}, protocols=[], strip=True) 
        super(Review, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.book_reviewed