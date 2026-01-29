from django.urls import path
from .views import login_view, PostListCreateView

urlpatterns = [
    path('auth/login/', login_view, name='login'),
    path('posts/', PostListCreateView.as_view(), name='posts'),
]
