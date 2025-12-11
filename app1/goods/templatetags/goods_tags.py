from django import template

from goods.models import Categories


register = template.Library()

@register.simple_tag()
def tag_categories():
    return Categories.objects.all()

# @register.simple_tag(takes_context=True)
# def charge_params(context, **kwargs):
#     querty = context['request'].GET.dict()
#     querty.update(kwargs)
#     return urldate(kwargs)
#     return urlencode(query)