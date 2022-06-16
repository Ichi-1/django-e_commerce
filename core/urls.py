from django.urls import path
from .views import (
    add_to_cart, CheckoutView, remove_from_cart,
    remove_single_item_from_cart,
    HomeView, ItemDetailView, OrderSummaryView,
    PaymentView
)
import string

app_name = 'core'

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('products/<slug>/', ItemDetailView.as_view(), name='products'),
    path('add-to-cart/<slug>', add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<slug>', remove_from_cart, name='remove-from-cart'),
    path('remove-item-from-cart/<slug>', remove_single_item_from_cart, name='remove-single-item-from-cart'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
]