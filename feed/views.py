from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

import json

from .models import Post, Comment, Interaction
from .serializers import PostSerializer


# --------------------------------------------------
# AUTH LOGIN
# --------------------------------------------------
@csrf_exempt
def login_view(request):
    if request.method != "POST":
        return JsonResponse({"error": "Only POST allowed"}, status=405)

    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)

    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return JsonResponse(
            {"error": "Username and password required"},
            status=400
        )

    # Demo-safe user creation
    user, created = User.objects.get_or_create(username=username)
    if created:
        user.set_password(password)
        user.save()

    user = authenticate(username=username, password=password)

    if user is None:
        return JsonResponse({"error": "Invalid credentials"}, status=401)

    return JsonResponse({"message": "Login successful"})


# --------------------------------------------------
# POSTS VIEWSET
# --------------------------------------------------
class PostViewSet(viewsets.ViewSet):

    # GET /api/posts/
    def list(self, request):
        posts = Post.objects.all().order_by("-created_at")
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    # POST /api/posts/
    def create(self, request):
        content = request.data.get("content")

        if not content:
            return Response(
                {"error": "Post content required"},
                status=400
            )

        post = Post.objects.create(content=content)
        serializer = PostSerializer(post)
        return Response(serializer.data, status=201)

    # POST /api/posts/{id}/comments/
    @action(detail=True, methods=["post"])
    def comments(self, request, pk=None):
        post = get_object_or_404(Post, pk=pk)
        content = request.data.get("comment")

        if not content:
            return Response(
                {"error": "Comment content required"},
                status=400
            )

        Comment.objects.create(
            post=post,
            content=content
        )

        return Response({"message": "Comment added"}, status=201)

    # POST /api/posts/{id}/like/
    @action(detail=True, methods=["post"])
    def like(self, request, pk=None):
        post = get_object_or_404(Post, pk=pk)

        Interaction.objects.create(
            post=post,
            interaction_type=Interaction.LIKE
        )

        return Response({"message": "Post liked"}, status=201)
