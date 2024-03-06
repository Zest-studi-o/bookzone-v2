from django.urls import path
from reviews import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    # Url path to reviews template -  CRUD USER - Add review



    path(
        'book/<int:book_id>/reviews/',
        views.book_reviews,
        name='book_reviews'
    ),
 
    path('update-review/<int:review_id>/', views.update_review, name='update_review'),

    
    path('delete-review/<int:pk>/', views.DeleteReview.as_view(), name='delete_review'), 
]
