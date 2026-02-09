from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Post, Comment, Interaction
from .serializers import PostSerializer


# -------------------------
# LOGIN VIEW
# -------------------------
@csrf_exempt
def login_view(request):
    if request.method != "POST":
        return JsonResponse({"error": "Only POST allowed"}, status=405)

    # Always ensure demo_user exists
    demo_user, _ = User.objects.get_or_create(username="demo_user")
    demo_user.set_password("DemoPass123")
    demo_user.save()

    try:
        data = json.loads(request.body)
    except Exception:
        return JsonResponse({"error": "Invalid JSON"}, status=400)

    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return JsonResponse(
            {"error": "Missing username or password"},
            status=400
        )

    user = authenticate(username=username, password=password)
    if not user:
        return JsonResponse({"error": "Invalid credentials"}, status=400)

    return JsonResponse({"message": "Login successful"})
    

# -------------------------
# POST VIEWSET
# -------------------------
class PostViewSet(viewsets.ModelViewSet):
    """
    Endpoints:
    ✅ GET    /api/posts/
    ✅ POST   /api/posts/
    ✅ POST   /api/posts/<id>/comments/
    ✅ POST   /api/posts/<id>/like/
    """
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        demo_user, _ = User.objects.get_or_create(username="demo_user")
        serializer.save(author=demo_user)

    # -------------------------
    # COMMENTS
    # -------------------------
    @action(detail=True, methods=['post'])
    def comments(self, request, pk=None):
        post = self.get_object()
        content = request.data.get("content")

        if not content:
            return Response(
                {"error": "Comment content is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        demo_user, _ = User.objects.get_or_create(username="demo_user")

        comment = Comment.objects.create(
            post=post,
            author=demo_user,
            content=content
        )

        return Response(
            {
                "id": comment.id,
                "post": post.id,
                "author": demo_user.username,
                "content": comment.content,
                "created_at": comment.created_at
            },
            status=status.HTTP_201_CREATED
        )

    # -------------------------
    # LIKE
    # -------------------------
    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        post = self.get_object()
        demo_user, _ = User.objects.get_or_create(username="demo_user")

        already_liked = Interaction.objects.filter(
            post=post,
            user=demo_user,
            interaction_type=Interaction.LIKE
        ).exists()

        if already_liked:
            return Response(
                {"message": "Post already liked"},
                status=status.HTTP_200_OK
            )

        Interaction.objects.create(
            post=post,
            user=demo_user,
            interaction_type=Interaction.LIKE
        )

        return Response(
            {"message": "Post liked successfully"},
            status=status.HTTP_201_CREATED
        )
