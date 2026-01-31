import graphene
from graphene_django import DjangoObjectType
from .models import Post, Comment, Interaction
from django.contrib.auth.models import User

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

class Query(graphene.ObjectType):
    all_posts = graphene.List(PostType)

    def resolve_all_posts(root, info):
        return Post.objects.all()

class CreatePost(graphene.Mutation):
    post = graphene.Field(PostType)

    class Arguments:
        content = graphene.String(required=True)

    def mutate(self, info, content):
        user = info.context.user
        post = Post.objects.create(author=user, content=content)
        return CreatePost(post=post)

class Mutation(graphene.ObjectType):
    create_post = CreatePost.Field()
