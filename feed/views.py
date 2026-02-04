# feed/views.py
from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def login_view(request):
    if request.method != "POST":
        return JsonResponse({"error": "Only POST allowed"}, status=405)
    
    data = json.loads(request.body)
    username = data.get("username")
    password = data.get("password")
    
    if not username or not password:
        return JsonResponse({"error": "Missing username or password"}, status=400)
    
    user = authenticate(username=username, password=password)
    if not user:
        return JsonResponse({"error": "Invalid credentials"}, status=400)
    
    return JsonResponse({"message": "Login successful"})
