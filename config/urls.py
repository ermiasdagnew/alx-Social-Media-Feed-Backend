# feed/urls.py
from django.urls import path
from .views import login_view, create_post_view, get_posts_view, comment_post_view, like_post_view

urlpatterns = [
    # Authentication
    path('auth/login/', login_view, name='login'),

    # Posts
    path('posts/', get_posts_view, name='get_posts'),       # GET all posts
    path('posts/', create_post_view, name='create_post'),   # POST new post

    # Comments
    path('posts/<int:id>/comments/', comment_post_view, name='comment_post'),

    # Likes
    path('posts/<int:id>/like/', like_post_view, name='like_post'),
]
