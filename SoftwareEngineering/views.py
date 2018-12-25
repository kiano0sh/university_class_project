from django.shortcuts import render


def index(request):
    if request.method == 'GET':
        context = {}
        return render(request, 'newApp/index.html', context=context)
