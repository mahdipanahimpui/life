"""
URL configuration for life project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import path, include, re_path
from django.contrib.sitemaps.views import sitemap
from home.views import robots_txt

from home.sitemaps import (
    StaticViewSitemap, 
    InvoiceProductsSitemap, 
    FlyerProductsSitemap, 
    PrescriptionProductsSitemap
)

sitemaps = {
    'static': StaticViewSitemap,
    'invoice_products': InvoiceProductsSitemap,
    'flyer_products': FlyerProductsSitemap,
    'prescription_products': PrescriptionProductsSitemap,
}

sitemaps = {
    'static': StaticViewSitemap,
    'invoice_products': InvoiceProductsSitemap,
    'flyer_products': FlyerProductsSitemap,
    'prescription_products': PrescriptionProductsSitemap,
}

urlpatterns = [
    path('aadmin/', admin.site.urls),
    path('', include('home.urls', namespace='home')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('products/', include('products.urls', namespace='products')),
    path('orders/', include('orders.urls', namespace='orders')),
    path('cart/', include('cart.urls', namespace='cart')),
    re_path(r'^tracking/', include('tracking.urls')),
    path('user/address/', include('addresses.urls', namespace='addresses')),
    path('user/orders_history/', include('history.urls', namespace='history')),
    path('extra/', include('extra.urls', namespace='extra')),

    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt', robots_txt, name='robots_txt')


]




