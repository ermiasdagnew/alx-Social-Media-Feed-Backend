from django.urls import path
from django.http import JsonResponse
from .views import (
    PostViewSet,
    login_view,
    add_comment,
    like_post,
)

post_list = PostViewSet.as_view({
    "get": "list",
    "post": "create",
})

post_detail = PostViewSet.as_view({
    "put": "update",
    "patch": "partial_update",
    "delete": "destroy",
})


def api_root(request):
    return JsonResponse({"message": "API is running"})


urlpatterns = [
    path("", api_root),

    # Auth
    path("auth/login/", login_view),

    # Posts
    path("posts/", post_list),
    path("posts/<int:pk>/", post_detail),

    # Comments & Likes (function-based)
    path("posts/<int:id>/comments/", add_comment),
    path("posts/<int:id>/like/", like_post),
]
