from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('cart/', views.cart, name='cart'),
    path('purchase/', views.purchase, name='purchase'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('buy_now/<int:product_id>/', views.buy_now, name='buy_now'),
]
