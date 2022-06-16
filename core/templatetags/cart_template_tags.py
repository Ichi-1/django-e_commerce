from django import template
from core.models import Order

register = template.Library()

@register.filter
def cart_item_count(user):
    if user.is_authenticated:
        qs = Order.objects.filter(
            user=user, 
            ordered=False,
        )
        if qs.exists():
            return qs[0].items.count()
    return 0


#TODO fix count in cart
# @register.filter
# def cart_item_count(user):
#     if user.is_authenticated:
#         total = 0
#         try:
#             order = OrderItem.objects.filter(user=user, ordered=False)
#             count = order.values('quantity')
#             for i in count:
#                 total += i['quantity']
#             return total
#         except:
#             return 0