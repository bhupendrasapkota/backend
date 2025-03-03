from django.http import JsonResponse

def collection_list(request):
    return JsonResponse({"message": "Collection list"})