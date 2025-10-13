from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, UpdateView, DetailView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from .models import Address
from .forms import AddressForm
from cart.models import DeliveryOption
from cart.models import ShoppingCart
from orders.models import InvoiceProductOrder, FlyerProductOrder, PrescriptionProductOrder


class AddressManageView(LoginRequiredMixin, UpdateView):
    model = Address
    form_class = AddressForm
    template_name = 'addresses/address.html'
    
    def get_success_url(self):
        return reverse_lazy('cart:delivery')
    
    def get_object(self, queryset=None):
        """برگرداندن آدرس کاربر یا ایجاد یک آدرس جدید اگر وجود ندارد"""
        obj, created = Address.objects.get_or_create(user=self.request.user)
        return obj
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        if self.object.pk:  # اگر آدرس موجود است (ویرایش)
            messages.success(self.request, "آدرس با موفقیت به‌روزرسانی شد.")
        else:  # اگر آدرس جدید است (ایجاد)
            messages.success(self.request, "آدرس با موفقیت ثبت شد.")
        return super().form_valid(form)
    
    def post(self, request, *args, **kwargs):
        # جلوگیری از حذف از طریق POST
        if 'delete' in request.POST:
            messages.error(request, "امکان حذف آدرس وجود ندارد. فقط می‌توانید آن را ویرایش کنید.")
            return self.get(request, *args, **kwargs)
        return super().post(request, *args, **kwargs)


# class AddressCreateView(LoginRequiredMixin, CreateView):
#     model = Address
#     form_class = AddressForm
#     template_name = 'addresses/address.html'
    
#     def get_success_url(self):
#         return reverse_lazy('cart:shopping_cart')
    
#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         messages.success(self.request, "آدرس با موفقیت ثبت شد.")
#         return super().form_valid(form)
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
        
    #     # دریافت سبد خرید پرداخت نشده
    #     shopping_cart = ShoppingCart.get_or_create_unpaid_cart(self.request.user)
        
    #     # محاسبه قیمت‌ها
    #     context.update(self.get_order_summary(shopping_cart))
    #     context['delivery_options'] = DeliveryOption.objects.all()
    #     context['shopping_cart'] = shopping_cart
        
    #     return context
    
    # def get_order_summary(self, shopping_cart):
    #     """محاسبه خلاصه سفارش"""
    #     # محاسبه قیمت سفارش‌ها
        
    #     total_product_price = shopping_cart.total_product_price
        
    #     # اگر delivery_option انتخاب شده، قیمت آن را اضافه کن
    #     delivery_price = shopping_cart.delivery_option.price if shopping_cart.delivery_option else 0
    #     price_to_pay = total_product_price + delivery_price
        
    #     return {
    #         'total_product_price': total_product_price,
    #         'delivery_price': delivery_price,
    #         'price_to_pay': price_to_pay,
    #     }