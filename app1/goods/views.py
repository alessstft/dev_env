from django.shortcuts import render, get_object_or_404
from django.shortcuts import render

from goods.models import Products


def catalog(request):
    
    goods = Products.objects.all

    context = {
        'title':'Каталог',
        'goods': goods,
    }
    return render(request, 'goods/catalog.html', context)


def product(request, product_id):

    product = Products.objects.get(id=product_id)
    
    product_item = get_object_or_404(Products, id=product_id)
    
    context = {
        'product': product,
    }
    return render(request, 'goods/product.html', context=context)