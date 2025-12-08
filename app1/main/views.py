from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context: dict = {
        "title" : "FreeCloth",
        "content":"Магазин одежды FreeCloth"
    }
    return render(request, 'main/index.html', context)
 
def about(request):
    context: dict = {
        "title" : "FreeCloth - о нас",
        "content":"О нас",
        "text_on_page": "Почему я самый лучший? Потому что!"
    }
    return render(request, 'main/about.html', context)

