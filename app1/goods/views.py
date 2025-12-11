from django.core.paginator import Paginator 
from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from goods.models import Products
from goods.utils import q_search


def catalog(request, category_slug=None):

    page = request.GET.get("page", 1)
    on_sale = request.GET.get("on_sale")
    order_by = request.GET.get("order_by")
    query = request.GET.get("q", "")

    goods = Products.objects.all()

    if query:
        goods = goods.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query) |
            Q(id__icontains=query) |
            Q(slug__icontains=query) |
            Q(category__name__icontains=query)
        )

    if category_slug and category_slug != "all":
        goods = goods.filter(category__slug=category_slug)

    if on_sale:
        goods = goods.filter(discount__gt=0)

    if order_by and order_by != "default":
        goods = goods.order_by(order_by)

    paginator = Paginator(goods, 9)
    goods = paginator.get_page(page)

    return render(request, "goods/catalog.html", {
        "title": "Каталог",
        "goods": goods,
        "category_slug": category_slug,
        "query": query,
        "on_sale": on_sale,
        "order_by": order_by,
    })



def product(request, product_slug):

    product = get_object_or_404(Products, slug=product_slug)
    

     
    context = {
        'product': product,
    }
    return render(request, 'goods/product.html', context=context)