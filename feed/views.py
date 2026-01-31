import json
from django.http import JsonResponse
from django.contrib.auth import authenticate

def login_view(request):
    # 1. Allow only POST
    if request.method != "POST":
        return JsonResponse(
            {"error": "Only POST method allowed"},
            status=405
        )

    # 2. Parse JSON body
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse(
            {"error": "Invalid JSON"},
            status=400
        )

    # 3. Get email & password
    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return JsonResponse(
            {"error": "email and password are required"},
            status=400
        )

    # 4. Authenticate user
    user = authenticate(username=email, password=password)

    if user is None:
        return JsonResponse(
            {"error": "Invalid email or password"},
            status=400
        )

    # 5. Success response
    return JsonResponse(
        {"message": "Login successful"},
        status=200
    )
