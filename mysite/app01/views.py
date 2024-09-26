from django.shortcuts import render, HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the app01 index.")


def user_list(request):
    return render(request, 'user_list.html')


def user_add(request):
    return render(request, 'user_add.html')
