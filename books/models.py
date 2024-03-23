from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import Avg


class CustomUser(AbstractUser):
    # Customised user attributes
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)


class Book(models.Model):
    sku = models.CharField(max_length=200, null=True, blank=True)
    isbn = models.CharField(max_length=13, null=True, blank=True)
    # ISBN are from 10 to 13
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    description = models.TextField(max_length=400)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    condition = models.CharField(max_length=50)
    # New, Like New, Good, Acceptable
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True)
    seller = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='books_for_sale')
    image = models.ImageField(upload_to='book_images/', blank=True, null=True)
    upload_date = models.DateTimeField(auto_now_add=True)

    def calculate_average_rating(self):
        """
        Average rating based on reviews
        """
        reviews = self.reviews.all()
        if reviews:
            total_rating = sum(review.rating for review in reviews)
            average_rating = total_rating / len(reviews)
            return round(average_rating, 2)
        else:
            return 1

    def update_rating(self):
        """
        Updates the rating based on reviews
        """
        average_rating = self.reviews.aggregate(Avg('rating'))['rating__avg']
        if average_rating is not None:
            self.rating = round(average_rating, 2)
        else:
            self.rating = 0
        self.save()

    def __str__(self):
        return self.title


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=100)
    friendly_name = models.CharField(max_length=254, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

    """

    def __str__(self):
        return f'{self.book.title} sold to {self.buyer.username} on {self.date}'

    def __str__(self):
        return f'Review by {self.user.username} for {self.book.title}'
    """