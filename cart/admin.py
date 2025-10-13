from django.contrib import admin
from django.utils.html import format_html
from .models import ShoppingCart, DeliveryOption, PaymentOption


@admin.register(ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = [
        'id', 
        'user',
        'is_paid', 
        'delivery_option',
        'payment_option',
        'card_number',
        'total_orders_count',
        'total_product_price',
        'delivery_price',
        'view_orders_link',
        'price_to_pay',
        'paid_price',
        'ref_code',
        'paid_at'
    ]

    list_filter = [
        'is_paid'
    ]

    def total_orders_count(self, obj):
        """تعداد کل Orderها از تمام انواع"""
        return (obj.invoice_orders.count() + 
                obj.flyer_orders.count() + 
                obj.prescription_orders.count())
    
    total_orders_count.short_description = 'Count of Orders'


    def view_orders_link(self, obj):
        """لینک‌های جداگانه برای مشاهده هر نوع Order"""
        invoice_count = obj.invoice_orders.count()
        flyer_count = obj.flyer_orders.count()
        prescription_count = obj.prescription_orders.count()
        
        total_count = invoice_count + flyer_count + prescription_count
        
        if total_count == 0:
            return format_html(
                '<span style="color: #999; font-style: italic;">No Orders</span>'
            )
        
        links = []
        
        # لینک سفارش‌های فاکتور
        if invoice_count > 0:
            invoice_url = f"/admin/orders/invoiceproductorder/?shopping_cart__id__exact={obj.id}"
            links.append(
                f'<a href="{invoice_url}" style="background-color: #2196F3; color: white; padding: 2px 6px; margin: 1px; text-decoration: none; border-radius: 3px; font-size: 11px; display: inline-block;">invoice: {invoice_count}</a>'
            )
        
        # لینک سفارش‌های فلایر
        if flyer_count > 0:
            flyer_url = f"/admin/orders/flyerproductorder/?shopping_cart__id__exact={obj.id}"
            links.append(
                f'<a href="{flyer_url}" style="background-color: #FF9800; color: white; padding: 2px 6px; margin: 1px; text-decoration: none; border-radius: 3px; font-size: 11px; display: inline-block;">flyer: {flyer_count}</a>'
            )
        
        # لینک سفارش‌های نسخه
        if prescription_count > 0:
            prescription_url = f"/admin/orders/prescriptionproductorder/?shopping_cart__id__exact={obj.id}"
            links.append(
                f'<a href="{prescription_url}" style="background-color: #9C27B0; color: white; padding: 2px 6px; margin: 1px; text-decoration: none; border-radius: 3px; font-size: 11px; display: inline-block;">prescription: {prescription_count}</a>'
            )
        
        
        return format_html(" ".join(links))
    
    view_orders_link.short_description = 'View Orders'



@admin.register(DeliveryOption)
class DeliveryOptionAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'description']



@admin.register(PaymentOption)
class PaymentOptionAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']