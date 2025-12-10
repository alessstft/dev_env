from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.core.paginator import Paginator

from goods.models import Products


def catalog(request):

    # on_sale = request.GET.get('on_sale', None)
    # order_by = request.GET.get('order_by', None)
    
    goods = Products.objects.all

    # if category_slug == "all":
    #     goods = Products.objects.all()
    # else:
    #     goods = get_list_or_404(Products.objects.filter(category__slug=category_slug))

    # if on_sale:
    #     goods = goods.filter(discount_gt=0)

    # if order_by and order_by != "default":
    #     goods = goods.order_by(order_by)



    # paginator = Paginator(goods, 3)
    # current_page = paginator.page(int(page)) 

    context = {
        'title':'Каталог',
        'goods': goods,
        # "slug_url": category_slug
    }
    return render(request, 'goods/catalog.html', context)


def product(request, product_id):
    product = Products.objects.get(id=product_id)

    context = {
        'product' : product
    }
    return render(request, 'goods/product.html', context=context)