from django.http import JsonResponse

def getRoute(request):
    return JsonResponse({ "msg": "Hello, World!" })