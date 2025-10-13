from django.contrib import admin


from .models import (
    PaperType,
    PaperSize,
    CirculationPrint,
    InvoiceType,
    InvoiceProduct,
    FlyerProduct,
    PrescriptionProduct,
    SideType,
    ColorMode
)

# ---------------------------------------------------------------------
@admin.register(PaperType)
class PaperTypeAdmin(admin.ModelAdmin):
    list_display = ['type',]


# ---------------------------------------------------------------------
@admin.register(PaperSize)
class PaperSizeAdmin(admin.ModelAdmin):
    list_display = ['size',]


# ---------------------------------------------------------------------
@admin.register(CirculationPrint)
class CirculationPrintAdmin(admin.ModelAdmin):
    list_display = ['circulation',]



# ---------------------------------------------------------------------
@admin.register(InvoiceType)
class InvoiceTypeAdmin(admin.ModelAdmin):
    list_display = ['type',]

# ---------------------------------------------------------------------
@admin.register(SideType)
class SydeTypeAdmin(admin.ModelAdmin):
    list_display = ['type',]

# ---------------------------------------------------------------------
@admin.register(ColorMode)
class ColorModeAdmin(admin.ModelAdmin):
    list_display = ['mode',]

# ---------------------------------------------------------------------
@admin.register(InvoiceProduct)
class InvoiceProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'paper_type', 'paper_size', 'color_mode', 'circulation', 'invoice_type', 'base_price']


# ---------------------------------------------------------------------
@admin.register(FlyerProduct)
class FlyerProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'paper_type', 'paper_size', 'color_mode', 'circulation', 'side', 'base_price']


# ---------------------------------------------------------------------
@admin.register(PrescriptionProduct)
class PrescriptionProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'paper_type', 'paper_size', 'circulation', 'base_price']



