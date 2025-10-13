from django.shortcuts import render
from django.views import View
import json

from .models import (
    PaperType,
    PaperSize,
    InvoiceType,
    CirculationPrint,
    InvoiceProduct,
    SideType,
    FlyerProduct,
    PrescriptionProduct,
    ColorMode
)


    

class InvoiceProductsView(View):
    """
    نمایش صفحه محصولات
    """
    template_name = 'products/invoice_products.html'

    def get(self, request):
        paper_types = PaperType.objects.all()
        paper_sizes = PaperSize.objects.all()
        invoice_types = InvoiceType.objects.all()
        circulations = CirculationPrint.objects.all()
        invoice_products = InvoiceProduct.objects.all()
        color_modes = ColorMode.objects.all()
        

        products_data = []
        for product in invoice_products:
            products_data.append({
                'product_type': 'invoice',
                'id': product.id,
                'title': product.title,
                'description': product.description,
                'paper_type': product.paper_type.type,
                'paper_size': product.paper_size.size,
                'color_mode': product.color_mode.mode,
                'invoice_type': product.invoice_type.type,
                'circulation': product.circulation.circulation,
                'base_price': float(product.base_price),
                'url': product.get_absolute_url()
            })
        
        context = {
            'product_type': 'invoice',
            'paper_types': paper_types,
            'paper_sizes': paper_sizes,
            'invoice_types': invoice_types,
            'color_modes': color_modes,
            'circulations': circulations,
            # 'invoice_products': invoice_products,
            'products_data': json.dumps(products_data, ensure_ascii=False)
        }
        
        return render(request, self.template_name, context)
    


class FlyerProductsView(View):
    """
    نمایش صفحه محصولات
    """
    template_name = 'products/flyer_products.html'

    def get(self, request):
        paper_types = PaperType.objects.all()
        paper_sizes = PaperSize.objects.all()
        side_types = SideType.objects.all()
        circulations = CirculationPrint.objects.all()
        flyer_products = FlyerProduct.objects.all()
        color_modes = ColorMode.objects.all()


        products_data = []
        for product in flyer_products:
            products_data.append({
                'product_type': 'flyer',
                'id': product.id,
                'title': product.title,
                'description': product.description,
                'paper_type': product.paper_type.type,
                'paper_size': product.paper_size.size,
                'color_mode': product.color_mode.mode,
                'side_type': product.side.type,
                'circulation': product.circulation.circulation,
                'base_price': float(product.base_price),
                'url': product.get_absolute_url()
            })
        
        context = {
            'product_type': 'flyer',
            'paper_types': paper_types,
            'paper_sizes': paper_sizes,
            'side_types': side_types,
            'color_modes': color_modes,
            'circulations': circulations,
            # 'flyer_products': flyer_products,
            'products_data': json.dumps(products_data, ensure_ascii=False)
        }
        
        return render(request, self.template_name, context)
    



class PrescriptionProductView(View):
    """
    نمایش صفحه محصولات
    """
    template_name = 'products/prescription_products.html'

    def get(self, request):
        paper_types = PaperType.objects.all()
        paper_sizes = PaperSize.objects.all()
        side_types = SideType.objects.all()
        circulations = CirculationPrint.objects.all()
        prescription_products = PrescriptionProduct.objects.all()
        color_modes = ColorMode.objects.all()

        products_data = []
        for product in prescription_products:
            products_data.append({
                'product_type': 'prescription',
                'id': product.id,
                'title': product.title,
                'description': product.description,
                'paper_type': product.paper_type.type,
                'paper_size': product.paper_size.size,
                'color_mode': product.color_mode.mode,
                'circulation': product.circulation.circulation,
                'base_price': float(product.base_price),
                'url': product.get_absolute_url()
            })
        
        context = {
            'product_type': 'prescription',
            'paper_types': paper_types,
            'paper_sizes': paper_sizes,
            'side_types': side_types,
            'color_modes': color_modes,
            'circulations': circulations,
            # 'prescription_products': prescription_products,
            'products_data': json.dumps(products_data, ensure_ascii=False)
        }
        
        return render(request, self.template_name, context)