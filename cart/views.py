from django.shortcuts import render, redirect, get_list_or_404
from django.urls import reverse_lazy
from django.utils import timezone
from django.views import View
from django.contrib import messages
from cart.models import ShoppingCart, DeliveryOption, PaymentOption
from django.views.generic import FormView
from addresses.models import Address
from .forms import DeliveryPaymentSelectionForm, CardToCardPaymentForm
from django.contrib.auth.mixins import LoginRequiredMixin







class ShoppingCartView(LoginRequiredMixin, View):
    template_name = 'cart/shopping_cart.html'
    
    def get(self, request):
        # دریافت یا ایجاد سبد خرید پرداخت نشده برای کاربر
        shopping_cart = self.get_or_create_unpaid_cart(request.user)
        
        # دریافت تمام سفارش‌های مربوط به این سبد خرید
        invoice_orders = shopping_cart.invoice_orders.all().order_by('-created_at')
        flyer_orders = shopping_cart.flyer_orders.all().order_by('-created_at')
        prescription_orders = shopping_cart.prescription_orders.all().order_by('-created_at')
        
        # محاسبه جمع قیمت‌ها
        total_invoice_price = sum(order.total_price for order in invoice_orders if order.total_price)
        total_flyer_price = sum(order.total_price for order in flyer_orders if order.total_price)
        total_prescription_price = sum(order.total_price for order in prescription_orders if order.total_price)
        
        total_product_price = total_invoice_price + total_flyer_price + total_prescription_price
        
        # به‌روزرسانی قیمت سبد خرید
        if total_product_price > 0 and shopping_cart.total_product_price != total_product_price:
            shopping_cart.total_product_price = total_product_price
            shopping_cart.save()

        # NOTE: design_option_price
        context = {
            'shopping_cart': shopping_cart,
            'invoice_orders': invoice_orders,
            'flyer_orders': flyer_orders,
            'prescription_orders': prescription_orders,
            'total_product_price': total_product_price,
        }
        return render(request, self.template_name, context)
    

    def get_or_create_unpaid_cart(self, user):
        """دریافت یا ایجاد سبد خرید پرداخت نشده"""
        try:
            # سعی کن سبد خرید پرداخت نشده موجود را پیدا کنی
            cart = ShoppingCart.objects.get(user=user, is_paid=False)
            return cart
        except ShoppingCart.DoesNotExist:
            # اگر وجود نداشت، یک سبد خرید جدید ایجاد کن
            cart = ShoppingCart.objects.create(user=user, is_paid=False)
            return cart
        
        except ShoppingCart.MultipleObjectsReturned:
            # اگر چند سبد خرید پرداخت نشده وجود داشت، اولین را برگردان و بقیه را حذف کن
            carts = ShoppingCart.objects.filter(user=user, is_paid=False)
            cart = carts.first()
            carts.exclude(pk=cart.pk).delete()
            return cart


# --------------------------------------------------------------------
class DeliveryPaymentView(LoginRequiredMixin, View):
    template_name = 'cart/delivery.html'
    form_class = DeliveryPaymentSelectionForm
    
    def get(self, request, *args, **kwargs):
        address = Address.objects.filter(user=request.user).first()


        if not address:
            return redirect('addresses:address_manage')
        
        context = {
            'address': address,
            'form': self.form_class,
            'delivery_options': DeliveryOption.objects.all(),
        }
        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        address = Address.objects.filter(user=request.user).first()
        
        if not address:
            return redirect('addresses:address_manage')
        
        if form.is_valid():
            shipping_option_id = form.cleaned_data.pop('shipping_method')
            delivery_option = DeliveryOption.objects.get(id=shipping_option_id)

            payment_option_id = form.cleaned_data.pop('payment_method')
            payment_option = PaymentOption.objects.get(id=payment_option_id)

            cart = ShoppingCart.objects.filter(user=request.user, is_paid=False).first()
            cart.delivery_option = delivery_option
            cart.delivery_price = delivery_option.price
            cart.payment_option = payment_option

            cart.save()
            cart.price_to_pay = cart.total_product_price + cart.delivery_price
            cart.save()
            
            if cart.payment_option.code == 0:
                return redirect('cart:card_to_card')
            elif cart.payment_option.code == 1:
                return redirect('cart:online_gateway')
            
            else:
                messages.error(self.request, "مشکلی در پرداخت پیش آمده، با پشتیبانی تماس بگیرید")
                return redirect('home:home')

            
        context = {
            'address': address,
            'form': form,
            'delivery_options': DeliveryOption.objects.all(),
        }
        return render(request, self.template_name, context)


    
# ----------------------------------------------------------------------------
class CardToCardView(LoginRequiredMixin, FormView):
    template_name = 'cart/card_to_card.html'
    form_class = CardToCardPaymentForm
    success_url = reverse_lazy('history:orders_history')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # فرض بر این است که شما اطلاعات سبد خرید (ShoppingCart) را می‌خواهید
        cart = ShoppingCart.objects.filter(user=self.request.user, is_paid=False).first()
        
        if cart:
            # جمع هزینه‌های سفارش و ارسال
            total_price = cart.price_to_pay  # هزینه سفارش (باید از مدل ShoppingCart به دست آید)

            # ارسال مقادیر به context
            context.update({
                'total_price': total_price,
            })
        else:
            # اگر سبد خرید پیدا نشد، مقادیر صفر را ارسال می‌کنیم
            context.update({
                'total_price': 0,
            })
        
        return context
    
    def form_valid(self, form):
        card_number = form.cleaned_data['card_number']
        tracking_code = form.cleaned_data['tracking_code']

        try:
            cart = ShoppingCart.objects.filter(user=self.request.user, is_paid=False).first()
            
            if not cart:
                messages.error(self.request, 'سبد خرید فعالی پیدا نشد.')
                return self.form_invalid(form)
            
            # آپدیت اطلاعات پرداخت
            cart.ref_code = tracking_code
            cart.card_number = card_number
            cart.paid_at = timezone.now()
            cart.is_paid = True
            cart.save()

            messages.success(self.request, 'اطلاعات پرداخت با موفقیت ثبت شد و سفارش شما تایید گردید.')
            return super().form_valid(form)
            
        except Exception as e:
            messages.error(self.request, f'خطا در ثبت اطلاعات پرداخت: {str(e)}')
            return self.form_invalid(form)






