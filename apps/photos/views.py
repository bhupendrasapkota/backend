from django.http import JsonResponse

def photo_list(request):
    return JsonResponse({"message": "Photo list"})