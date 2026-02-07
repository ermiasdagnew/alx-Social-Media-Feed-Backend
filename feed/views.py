from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from rest_framework import viewsets, permissions
from django.shortcuts import get_object_or_404
from .models import Post, Comment, Interaction
from .serializers import PostSerializer


# -------------------------
# Login View
# -------------------------
@csrf_exempt
def login_view(request):
    if request.method != "POST":
        return JsonResponse({"error": "Only POST allowed"}, status=405)

    # Ensure demo_user exists and password is always correct
    demo_user, created = User.objects.get_or_create(username="demo_user")
    demo_user.set_password("DemoPass123")
    demo_user.save()

    try:
        data = json.loads(request.body)
    except:
        return JsonResponse({"error": "Invalid JSON"}, status=400)

    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return JsonResponse({"error": "Missing username or password"}, status=400)

    user = authenticate(username=username, password=password)
    if not user:
        return JsonResponse({"error": "Invalid credentials"}, status=400)

    return JsonResponse({"message": "Login successful"})


# -------------------------
# Post ViewSet
# -------------------------
class PostViewSet(viewsets.ModelViewSet):
    """
    Handles:
    - GET /api/posts/        → List all posts
    - POST /api/posts/       → Create new post (auto assigns demo_user as author)
    - PUT/PATCH /api/posts/<id>/ → Update post
    - DELETE /api/posts/<id>/ → Delete post
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.AllowAny]  # no auth needed for demo

    def perform_create(self, serializer):
        # Automatically assign demo_user as author
        demo_user, _ = User.objects.get_or_create(username="demo_user")
        serializer.save(author=demo_user)


# -------------------------
# Add Comment to a Post
# -------------------------
@csrf_exempt
def add_comment(request, id):
    if request.method != "POST":
        return JsonResponse({"error": "Only POST allowed"}, status=405)

    post = get_object_or_404(Post, id=id)
    demo_user, _ = User.objects.get_or_create(username="demo_user")

    try:
        data = json.loads(request.body)
        content = data.get("content") or data.get("comment")
    except:
        return JsonResponse({"error": "Invalid JSON"}, status=400)

    comment = Comment.objects.create(post=post, author=demo_user, content=content)
    return JsonResponse({
        "id": comment.id,
        "post": comment.post.id,
        "author": comment.author.username,
        "content": comment.content,
        "created_at": comment.created_at
    })


# -------------------------
# Like a Post
# -------------------------
@csrf_exempt
def like_post(request, id):
    if request.method != "POST":
        return JsonResponse({"error": "Only POST allowed"}, status=405)

    post = get_object_or_404(Post, id=id)
    demo_user, _ = User.objects.get_or_create(username="demo_user")

    # Prevent duplicate likes
    if Interaction.objects.filter(post=post, user=demo_user, interaction_type="LIKE").exists():
        return JsonResponse({"message": "Post already liked"})

    Interaction.objects.create(post=post, user=demo_user, interaction_type="LIKE")
    return JsonResponse({"message": "Post liked"})
