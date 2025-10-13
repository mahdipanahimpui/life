from django.urls import path
from . import views


app_name = 'orders'

urlpatterns = [
    path('invoice-order/create/<str:slug>/', views.InvoiceProductOrderCreateView.as_view(), name='invoice_order_create'),
    path('invoice-order/delete/<int:id>/', views.InvoiceProductOrderDeleteView.as_view(), name='invoice_order_delete'),
    path('flyer-order/create/<str:slug>/', views.FlyerProductOrderCreateView.as_view(), name='flyer_order_create'),
    path('flyer-order/delete/<int:id>/', views.FlyerProductOrderDeleteView.as_view(), name='flyer_order_delete'),
    path('prescription-order/create/<str:slug>/', views.PrescriptionProductOrderCreateView.as_view(), name='prescription_order_create'),
    path('prescription-order/delete/<int:id>/', views.PrescriptionProductOrderDeleteView.as_view(), name='prescription_order_delete')
]
