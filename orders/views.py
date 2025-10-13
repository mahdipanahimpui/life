from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.forms import ValidationError
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views import View
from django.utils.decorators import method_decorator
from accounts.utils import count_view

from django.views.generic import CreateView

from .forms import InvoiceProductOrderForm, FlyerProductOrderForm, PrescriptionProductOrderForm
from products.models import InvoiceProduct, FlyerProduct, PrescriptionProduct
from cart.models import ShoppingCart

from .models import (
    InvoiceProductOrder,  
    FlyerProductOrder,
    PrescriptionProductOrder,
    AdditionalService, 
    BindingType, 
    BindingDirection, 
    DesignOption, 
    Color,
    
)

#  ------------------------------------------------------------------------------------
class InvoiceProductOrderCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = InvoiceProductOrder
    form_class = InvoiceProductOrderForm
    template_name = 'orders/invoice_order_create.html'
    success_message = "سفارش شما با موفقیت ثبت شد!"

    @method_decorator(count_view("invoice"))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get_success_url(self):
        return reverse_lazy('cart:shopping_cart')
    
    def get_initial(self):
        initial = super().get_initial()
        # دریافت invoice_product از طریق slug
        slug = self.kwargs.get('slug')
        if slug:
            invoice_product = get_object_or_404(InvoiceProduct, slug=slug)
            initial['invoice_product'] = invoice_product

        return initial
    
    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        # دریافت invoice_product از طریق slug
        slug = self.kwargs.get('slug')
        invoice_product = get_object_or_404(InvoiceProduct, slug=slug)
        
        # اضافه کردن داده‌های اضافی برای نمایش در تمپلیت
        context['invoice_product'] = invoice_product
        context['additional_services'] = AdditionalService.objects.filter(type='invoice')
        context['binding_types'] = BindingType.objects.all()
        context['binding_directions'] = BindingDirection.objects.all()
        context['desing_price'] = DesignOption.objects.filter(type='invoice').first().price
        context['colors'] = Color.objects.all()

        return context
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        
        # تنظیم invoice_product از طریق slug
        slug = self.kwargs.get('slug')
        invoice_product = get_object_or_404(InvoiceProduct, slug=slug)
        form.instance.invoice_product = invoice_product
        
        try:
            shopping_cart = ShoppingCart.get_or_create_unpaid_cart(self.request.user)
            form.instance.shopping_cart = shopping_cart
        except ValidationError as e:
            form.add_error(None, str(e))
            return self.form_invalid(form)
        

        return super().form_valid(form)


# -------------------------------------------------------------------------------------------------
class InvoiceProductOrderDeleteView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        obj = get_object_or_404(InvoiceProductOrder, id=kwargs['id'])
        obj.delete()        
        return redirect('cart:shopping_cart')
    

# --------------------------------------------------------------------------------------------
class FlyerProductOrderCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = FlyerProductOrder
    form_class = FlyerProductOrderForm
    template_name = 'orders/flyer_order_create.html'
    success_message = "سفارش شما با موفقیت ثبت شد!"

    @method_decorator(count_view("flyer"))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get_success_url(self):
        return reverse_lazy('cart:shopping_cart')
    
    def get_initial(self):
        initial = super().get_initial()
        # دریافت flyer_product از طریق slug
        slug = self.kwargs.get('slug')
        if slug:
            flyer_product = get_object_or_404(FlyerProduct, slug=slug)
            initial['flyer_product'] = flyer_product
        return initial
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # دریافت flyer_product از طریق slug
        slug = self.kwargs.get('slug')
        flyer_product = get_object_or_404(FlyerProduct, slug=slug)
        
        # اضافه کردن داده‌های اضافی برای نمایش در تمپلیت
        context['flyer_product'] = flyer_product
        context['additional_services'] = AdditionalService.objects.filter(type='flyer')

        if flyer_product.side.num == 1:
            context['desing_price'] = DesignOption.objects.filter(type='flyer_one_side').first().price

        elif flyer_product.side.num == 2:
            context['desing_price'] = DesignOption.objects.filter(type='flyer_two_side').first().price
        
        else:
            context['desing_price'] = DesignOption.objects.filter(type='flyer_two_side').first().price

        return context
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        
        # تنظیم flyer_product از طریق slug
        slug = self.kwargs.get('slug')
        flyer_product = get_object_or_404(FlyerProduct, slug=slug)
        form.instance.flyer_product = flyer_product

        try:
            shopping_cart = ShoppingCart.get_or_create_unpaid_cart(self.request.user)
            form.instance.shopping_cart = shopping_cart
        except ValidationError as e:
            form.add_error(None, str(e))
            return self.form_invalid(form)
            
        return super().form_valid(form)
    


# --------------------------------------------------------------------------------
class FlyerProductOrderDeleteView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        obj = get_object_or_404(FlyerProductOrder, id=kwargs['id'])
        obj.delete()        
        return redirect('cart:shopping_cart')
    


#  -------------------------------------------------------------------------
class PrescriptionProductOrderCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = PrescriptionProductOrder
    form_class = PrescriptionProductOrderForm
    template_name = 'orders/prescription_order_create.html'
    success_message = "سفارش شما با موفقیت ثبت شد!"

    @method_decorator(count_view("prescription"))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get_success_url(self):
        return reverse_lazy('cart:shopping_cart')
    
    def get_initial(self):
        initial = super().get_initial()
        # دریافت prescription_product از طریق slug
        slug = self.kwargs.get('slug')
        if slug:
            prescription_product = get_object_or_404(PrescriptionProduct, slug=slug)
            initial['prescription_product'] = prescription_product
        return initial
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # دریافت prescription_product از طریق slug
        slug = self.kwargs.get('slug')
        prescription_product = get_object_or_404(PrescriptionProduct, slug=slug)
        
        # اضافه کردن داده‌های اضافی برای نمایش در تمپلیت
        context['prescription_product'] = prescription_product
        context['additional_services'] = AdditionalService.objects.filter(type='invoice')
        context['binding_directions'] = BindingDirection.objects.all()
        context['desing_price'] = DesignOption.objects.filter(type='prescription').first().price
        return context
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        
        # تنظیم prescription_product از طریق slug
        slug = self.kwargs.get('slug')
        prescription_product = get_object_or_404(PrescriptionProduct, slug=slug)
        form.instance.prescription_product = prescription_product

        try:
            shopping_cart = ShoppingCart.get_or_create_unpaid_cart(self.request.user)
            form.instance.shopping_cart = shopping_cart
        except ValidationError as e:
            form.add_error(None, str(e))
            return self.form_invalid(form)
            
        return super().form_valid(form)
    

# --------------------------------------------------------------------------------
class PrescriptionProductOrderDeleteView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        obj = get_object_or_404(PrescriptionProductOrder, id=kwargs['id'])
        obj.delete()        
        return redirect('cart:shopping_cart')
    