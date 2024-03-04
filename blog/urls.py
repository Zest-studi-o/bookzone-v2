from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='blog'),
    path('post_add/', views.add_post, name='post_add'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('post_edit/<slug:slug>/', views.update_post, name='post_edit'),
    path('post_delete/<slug:slug>/', views.delete_post, name='post_delete'),
]