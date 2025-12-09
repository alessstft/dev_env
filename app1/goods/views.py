from django.shortcuts import render


def catalog(request):
    context = {
        'title':'Каталог',
        'goods': [
    {'image': 'deps/images/goods/mens_suit_black.jpg',
     'name': 'Костюм мужской черный',
     'description': 'Классический деловой костюм черного цвета.',
     'price': 280.00,
     'category': 'костюмы'},

    {'image': 'deps/images/goods/leather_jacket_black.jpg',
     'name': 'Кожаная куртка черная',
     'description': 'Классическая кожаная куртка черного цвета.',
     'price': 350.00,
     'category': 'куртки'},
     
    {'image': 'deps/images/goods/shirt_white.jpg',
     'name': 'Рубашка белая',
     'description': 'Классическая белая рубашка из хлопка.',
     'price': 50.00,
     'category': 'рубашки'},

    {'image': 'deps/images/goods/evening_dress.jpg',
     'name': 'Платье вечернее',
     'description': 'Длинное вечернее платье для торжеств.',
     'price': 190.00,
     'category': 'платья'},

    {'image': 'deps/images/goods/hoodie_gray.jpg',
     'name': 'Толстовка серая',
     'description': 'Серая толстовка с капюшоном из мягкого материала.',
     'price': 70.00,
     'category': 'кофты'},
     
    {'image': 'deps/images/goods/jeans_blue.jpg',
     'name': 'Джинсы синие',
     'description': 'Классические синие джинсы прямого кроя.',
     'price': 80.00,
     'category': 'штаны'},
     
]
    }
    return render(request, 'goods/catalog.html', context)


def product(request):
    return render(request, 'goods/product.html')