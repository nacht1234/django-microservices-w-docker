from django.http import JsonResponse

# Create your views here.
def product_service(request):
    return JsonResponse({
        "service": "Product Service",
        "status": "running",
    })