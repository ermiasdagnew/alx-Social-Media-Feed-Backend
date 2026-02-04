from django.urls import path
from django.http import JsonResponse
from .views import login_view

def api_root(request):
    return JsonResponse({"message": "API is running"})

urlpatterns = [
    path('', api_root),                 # http://127.0.0.1:8000/api/
    path('auth/login/', login_view, name='login'),  # http://127.0.0.1:8000/api/auth/login/
]
