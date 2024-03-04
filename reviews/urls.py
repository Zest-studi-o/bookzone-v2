from django.urls import path
from reviews import views

urlpatterns = [
    # Url path to reviews template
    path(
        'book/<int:book_id>/reviews/',
        views.book_reviews,
        name='book_reviews'
    ),
]