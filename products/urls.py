from django.urls import path
from . import views


app_name = 'products'
urlpatterns = [
    path('invoice/', views.InvoiceProductsView.as_view(), name='invoice_products'),
    path('flyer/', views.FlyerProductsView.as_view(), name='flyer_products'),
    path('prescription/', views.PrescriptionProductView.as_view(), name='prescription_products'),

]

