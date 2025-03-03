from django.http import JsonResponse

def follower_list(request):
    return JsonResponse({"message": "Follower list"})