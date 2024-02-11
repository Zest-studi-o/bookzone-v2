from django.contrib.auth.models import AbstractUser
from django.db import models


# Custom models
class CustomUser(AbstractUser):
    # Customised user attributes
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

class Book(models.Model):
    # isbn = models.DecimalField(max_digits=50, decimal_places=2, null=True, blank=True)
    isbn = models.CharField(max_length=100, null=True, blank=True)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    condition = models.CharField(max_length=50)  # New, Like New, Good, Acceptable
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True)
    seller = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='books_for_sale')
    image = models.ImageField(upload_to='book_images/', blank=True, null=True)
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=100)
    friendly_name = models.CharField(max_length=254,blank=True, null=True )
    description = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.name

class Transaction(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='transactions')
    buyer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='purchases')
    sale_price = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.book.title} sold to {self.buyer.username} on {self.date}'

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='reviews')
    content = models.TextField()
    rating = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Review by {self.user.username} for {self.book.title}'