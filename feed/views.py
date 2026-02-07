from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from rest_framework import viewsets, permissions
from .models import Post
from .serializers import PostSerializer

# -------------------------
# Login View
# -------------------------
@csrf_exempt
def login_view(request):
    if request.method != "POST":
        return JsonResponse({"error": "Only POST allowed"}, status=405)

    # Create demo_user safely if it doesn't exist
    if not User.objects.filter(username="demo_user").exists():
        User.objects.create_user(username="demo_user", password="DemoPass123")

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
