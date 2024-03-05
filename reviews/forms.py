from django import forms
from .models import Review
import crispy_forms
from django.utils.safestring import mark_safe


class ReviewForm(forms.ModelForm):
    """
    Crate and update a book review
    Fields to comment and rate
    """
    class Meta:
        model = Review
        fields = ['rating', 'content']
        exclude = ['reviewer']

    rating = forms.ChoiceField(
        choices=[
            (1, '1'),
            (2, '2'),
            (3, '3'),
            (4, '4'),
            (5, '5')
        ],
        required=True,
        widget=forms.Select(attrs={'class': 'form-control'}),
    )
    rating.label = mark_safe(
        '<i class="fa-solid fa-star" style="color: #ffaa3b;"></i> Star Rating'
    )

    content = forms.CharField(
        widget=forms.Textarea(
            attrs={'class': 'form-control', 'rows': '4'}
        ),
        required=True,
    )
    content.label = mark_safe(
        '<i class="fa-solid fa-comment" \
            style="color: #504939;"></i> Review Now'
    )