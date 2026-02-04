import graphene
from graphene_django import DjangoObjectType
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import Post, Comment, Interaction

# -------------------------------
# GraphQL Types
# -------------------------------

class PostType(DjangoObjectType):
    class Meta:
        model = Post
        fields = '__all__'

class CommentType(DjangoObjectType):
    class Meta:
        model = Comment
        fields = '__all__'

class InteractionType(DjangoObjectType):
    class Meta:
        model = Interaction
        fields = '__all__'

# -------------------------------
# Queries
# -------------------------------

class Query(graphene.ObjectType):
    all_posts = graphene.List(PostType)
    all_comments = graphene.List(CommentType)
    all_interactions = graphene.List(InteractionType)

    def resolve_all_posts(root, info):
        return Post.objects.all()

    def resolve_all_comments(root, info):
        return Comment.objects.all()

    def resolve_all_interactions(root, info):
        return Interaction.objects.all()

# -------------------------------
# Mutations
# -------------------------------

# Create Post
class CreatePost(graphene.Mutation):
    post = graphene.Field(PostType)

    class Arguments:
        content = graphene.String(required=True)

    def mutate(self, info, content):
        user = info.context.user
        if not user.is_authenticated:
            raise Exception("Authentication required")
        post = Post.objects.create(author=user, content=content)
        return CreatePost(post=post)

# Login Mutation
class LoginMutation(graphene.Mutation):
    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)

    success = graphene.Boolean()
    message = graphene.String()

    def mutate(self, info, username, password):
        user = authenticate(username=username, password=password)
        if not user:
            return LoginMutation(success=False, message="Invalid credentials")
        return LoginMutation(success=True, message="Login successful")

# Root Mutation
class Mutation(graphene.ObjectType):
    create_post = CreatePost.Field()
    login = LoginMutation.Field()

# -------------------------------
# Schema
# -------------------------------

schema = graphene.Schema(query=Query, mutation=Mutation)
