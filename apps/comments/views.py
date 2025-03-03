from django.http import JsonResponse

def comment_list(request):
    return JsonResponse({"message": "Comment list"})