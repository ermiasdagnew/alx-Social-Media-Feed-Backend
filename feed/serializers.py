# feed/serializers.py
from rest_framework import serializers
from .models import Post, Comment, Interaction

# -------------------------
# Post Serializer
# -------------------------
class PostSerializer(serializers.ModelSerializer):
    # Show the author's username instead of the full User object
    author = serializers.CharField(source='author.username', read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'author', 'content', 'created_at']
        read_only_fields = ['id', 'author', 'created_at']


# -------------------------
# Comment Serializer (optional)
# -------------------------
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'content', 'created_at']
        read_only_fields = ['id', 'author', 'created_at']


# -------------------------
# Interaction Serializer (optional)
# -------------------------
class InteractionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interaction
        fields = ['id', 'user', 'post', 'interaction_type', 'created_at']
        read_only_fields = ['id', 'created_at']
