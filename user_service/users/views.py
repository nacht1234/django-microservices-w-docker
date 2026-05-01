from django.http import JsonResponse

# Create your views here.
def user_service(request):
    return JsonResponse({
        "service": "User Service",
        "status": "running",
    })