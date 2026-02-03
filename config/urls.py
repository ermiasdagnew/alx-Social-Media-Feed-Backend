from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt

def home(request):
    return HttpResponse("Server is running!")

urlpatterns = [
    path('', home),  # <-- new home page
    path('admin/', admin.site.urls),
    path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True))),
]
