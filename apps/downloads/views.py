from django.http import JsonResponse

def download_list(request):
    return JsonResponse({"message": "Download list"})