from django.urls import path
from . import views


app_name = 'cart'

urlpatterns = [
    path('', views.ShoppingCartView.as_view(), name='shopping_cart'),
    path('delivery/', views.DeliveryPaymentView.as_view(), name='delivery'),
    path('card_to_card/', views.CardToCardView.as_view(), name='card_to_card'),

]