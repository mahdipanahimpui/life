# home/sitemaps.py
from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from products.models import InvoiceProduct, FlyerProduct, PrescriptionProduct

class StaticViewSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return [
            'home:home',
            'products:invoice_products', 
            'products:flyer_products',
            'products:prescription_products',
            'extra:about_us',
            'extra:contact_us',
            'extra:terms',
        ]

    def location(self, item):
        return reverse(item)

class InvoiceProductsSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.9

    def items(self):
        return InvoiceProduct.objects.all()

    def lastmod(self, obj):
        return obj.updated_at if hasattr(obj, 'updated_at') else obj.created_at

class FlyerProductsSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.9

    def items(self):
        return FlyerProduct.objects.all()

    def lastmod(self, obj):
        return obj.updated_at if hasattr(obj, 'updated_at') else obj.created_at

class PrescriptionProductsSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.9

    def items(self):
        return PrescriptionProduct.objects.all()