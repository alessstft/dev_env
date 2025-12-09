from django.shortcuts import render
from django.http import HttpResponse

from goods.models import Categories



def index(request):

    categories = Categories.objects.all()

    context: dict = {
        "title" : "FreeCloth",
        "content":"Магазин одежды FreeCloth",
        'categories' : categories
    }
    return render(request, 'main/index.html', context)
 
def about(request):
    context: dict = {
        "title" : "FreeCloth - о нас",
        "content":"О нас",
        "text_on_page": "Почему я самый лучший? Потому что!"
    }
    return render(request, 'main/about.html', context)

