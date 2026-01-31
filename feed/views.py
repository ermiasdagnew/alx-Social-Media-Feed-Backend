from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

from .models import Post
from .serializers import PostSerializer


@api_view(['POST'])
def login_view(request):
    user = authenticate(
        username=request.data.get("username"),  # or "email" if custom auth
        password=request.data.get("password")
    )
    if user:
        refresh = RefreshToken.for_user(user)
        return Response({
            "access": str(refresh.access_token)
        })
    return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)


class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
