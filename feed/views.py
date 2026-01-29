from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken

from .models import Post
from .serializers import PostSerializer


def login_view(request):
    user = authenticate(
        username=request.data.get("email"),
        password=request.data.get("password")
    )
    if user:
        refresh = RefreshToken.for_user(user)
        return Response({
            "access": str(refresh.access_token)
        })
    return Response({"error": "Invalid credentials"}, status=400)


class PostListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
