from django.http import JsonResponse

def photo_category_list(request):
    return JsonResponse({"message": "Photo category list"})