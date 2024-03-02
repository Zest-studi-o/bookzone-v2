from .models import Review
from django import forms


class ReviewForm(forms.ModelForm):
    """
    Review form class
    Allows to write a review
    """
    class Meta:
        model = Review
        fields = ('review_title', 'book_reviewed', 'content', 'rating')