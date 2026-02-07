from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'content', 'created_at', 'author']
        read_only_fields = ['author', 'id', 'created_at']  # author is auto-assigned
