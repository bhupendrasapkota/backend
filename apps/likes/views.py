from django.http import JsonResponse

def like_list(request):
    return JsonResponse({"message": "Like list"})