from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, login_view, add_comment, like_post
from django.http import JsonResponse

# API root: /api/
def api_root(request):
    return JsonResponse({"message": "API is running"})

# DRF router for posts
router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')

# URL patterns
urlpatterns = [
    path('', api_root),                     # /api/
    path('auth/login/', login_view, name='login'),  # /api/auth/login/
    path('', include(router.urls)),         # /api/posts/ handled by PostViewSet
    path('posts/<int:id>/comments/', add_comment, name='add_comment'),  # /api/posts/1/comments/
    path('posts/<int:id>/like/', like_post, name='like_post'),           # /api/posts/1/like/
]
