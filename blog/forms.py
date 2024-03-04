from .models import Post
from django import forms


class PostForm(forms.ModelForm):
    """
    To write a review
    """
    class Meta:
        model = Post
        fields = ('title', 'slug', 'section', 'content', 'excerpt', 'image', 'status') 