from . import views
from django.urls import path
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.ReviewList.as_view(), name='reviews'),
    path(
        'add-review/<str:order_number>/',
        login_required(views.ReviewCreateView.as_view()),
        name='add_review'
    ),
    path('update-review/<int:review_id>/', views.update_review, name='update_review'),  # noqa E501
    path('delete-review/<int:pk>/', views.DeleteReview.as_view(), name='delete_review'),  # noqa E501
]