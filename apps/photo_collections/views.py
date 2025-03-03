from django.http import JsonResponse

def photo_collection_list(request):
    return JsonResponse({"message": "Photo collection list"})