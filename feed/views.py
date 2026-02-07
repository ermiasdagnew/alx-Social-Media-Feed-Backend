from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def login_view(request):
    if request.method != "POST":
        return JsonResponse({"error": "Only POST allowed"}, status=405)

    # Create demo_user safely if it doesn't exist
    if not User.objects.filter(username="demo_user").exists():
        User.objects.create_user(username="demo_user", password="DemoPass123")

    try:
        data = json.loads(request.body)
    except:
        return JsonResponse({"error": "Invalid JSON"}, status=400)

    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return JsonResponse({"error": "Missing username or password"}, status=400)

    user = authenticate(username=username, password=password)
    if not user:
        return JsonResponse({"error": "Invalid credentials"}, status=400)

    return JsonResponse({"message": "Login successful"})
