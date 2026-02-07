from rest_framework import serializers
from .models import Post, Comment, Interaction

# -------------------------
# Post Serializer
# -------------------------
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'author', 'content', 'created_at']
        read_only_fields = ['id', 'author', 'created_at']  # author auto-assigned

# -------------------------
# Comment Serializer (optional)
# -------------------------
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'content', 'created_at']
        read_only_fields = ['id', 'author', 'created_at']  # optional: assign author automatically if needed

# -------------------------
# Interaction Serializer (optional)
# -------------------------
class InteractionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interaction
        fields = ['id', 'user', 'post', 'interaction_type', 'created_at']
        read_only_fields = ['id', 'created_at']  # user can be assigned automatically if needed
