from django.contrib import admin

from .models import (

    BindingType,
    BindingDirection,
    Color,
    AdditionalService, 
    DesignOption,
    InvoiceProductOrder,
    FlyerProductOrder,
    PrescriptionProductOrder
)


# ---------------------------------------------------------------------
@admin.register(BindingType)
class BindingTypeAdmin(admin.ModelAdmin):
    list_display = ['type',]


# ---------------------------------------------------------------------
@admin.register(BindingDirection)
class BindingDirectionAdmin(admin.ModelAdmin):
    list_display = ['direction',]


# ---------------------------------------------------------------------
@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ['name', 'code']


# ---------------------------------------------------------------------
@admin.register(AdditionalService)
class AdditionalServiceAdmin(admin.ModelAdmin):
    list_display = ['service', 'price']


# ---------------------------------------------------------------------
@admin.register(DesignOption)
class DesingOptionAdmin(admin.ModelAdmin):
    list_display = ['price',]




# ---------------------------------------------------------------------
@admin.register(InvoiceProductOrder)
class InvoiceProductOrderAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'user',
        'status',
        # 'is_paid',
        'invoice_product',
        'binding_type',
        'binding_direction',
        'with_number', 
        'start_from', 
        'color',
        'design_requirement',
        'get_additional_services',
        'file',
        'total_price',
        'created_at'
    ]

    def get_additional_services(self, obj):
        """متد custom برای نمایش سرویس‌های اضافی"""
        services = obj.additional_services.all()
        if services:
            return ", ".join([str(service) for service in services])
        return "هیچ سرویسی انتخاب نشده"
    
    get_additional_services.short_description = 'additional_services'


    search_fields = ['user__phone_number',]

    list_filter = [
        'status',
    ]

# ---------------------------------------------------------------------
@admin.register(FlyerProductOrder)
class FlyerProductOrderAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'user',
        'status',
        # 'is_paid',
        'flyer_product',
        'design_requirement',
        'get_additional_services',
        'file_front',
        'file_back',
        'total_price',
        'created_at'
    ]

    def get_additional_services(self, obj):
        """متد custom برای نمایش سرویس‌های اضافی"""
        services = obj.additional_services.all()
        if services:
            return ", ".join([str(service) for service in services])
        return "هیچ سرویسی انتخاب نشده"
    
    get_additional_services.short_description = 'additional_services'


    search_fields = ['user__phone_number',]

    list_filter = [
        'status', 
    ]

    



# ---------------------------------------------------------------------
@admin.register(PrescriptionProductOrder)
class PrescriptionProductOrderAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'user',
        'status',
        # 'is_paid',
        'prescription_product',
        'glue_attach',
        'binding_direction',
        'design_requirement',
        'get_additional_services',
        'file',
        'total_price',
        'created_at'
    ]

    def get_additional_services(self, obj):
        """متد custom برای نمایش سرویس‌های اضافی"""
        services = obj.additional_services.all()
        if services:
            return ", ".join([str(service) for service in services])
        return "هیچ سرویسی انتخاب نشده"
    
    get_additional_services.short_description = 'additional_services'


    search_fields = ['user__phone_number',]

    list_filter = [
        'status',
    ]