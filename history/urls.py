from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'history'
urlpatterns = [
    path('', views.OrdersHistoryView.as_view(), name='orders_history'),
]

