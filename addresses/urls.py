from django.urls import path
from . import views


app_name = 'addresses'

urlpatterns = [
    path('', views.AddressManageView.as_view(), name='address_manage'),
    # path('', views.AddressCreateView.as_view(), name='user_address'),
    # path('', views.AddressDetailView.as_view(), name='address_'),
    # path('', views.AddressUpdateView.as_view(), name='address_update')

]
