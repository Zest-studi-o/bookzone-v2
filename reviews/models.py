from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.db.models import Avg
from books.models import Book
from checkout.models import Order
from django.core.validators import MaxValueValidator, MinValueValidator
# to import the custom user
from django.conf import settings


class Review(models.Model):
    """
    Review for the books,
    the reviewer is the user who
    can add a rating and leave a comment
    """
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name='reviews', null=True
    )
    reviewer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    order = models.ForeignKey(
        Order, null=True,
        on_delete=models.SET_NULL,
        default=None
    )
    rating = models.PositiveIntegerField(
        default=0,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0)
        ]
     )
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.book.title} by {self.reviewer}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.book.update_rating()


@receiver(post_save, sender=Review)
@receiver(post_delete, sender=Review)
def update_book_rating(sender, instance, **kwargs):
    """
    To update the reviews when deleted or updated
    """
    instance.book.update_rating()
