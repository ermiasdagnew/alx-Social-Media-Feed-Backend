from django.urls import path
from .views import login_view
from django.http import JsonResponse

def api_root(request):
    return JsonResponse({"message": "API is running"})

urlpatterns = [
    path('', api_root),                     # /api/
    path('auth/login/', login_view, name='login'),  # /api/auth/login/
]
