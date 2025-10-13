from django.shortcuts import render

from django.views import View

from django.shortcuts import render, redirect
from django.views import View
from django.utils import timezone
from datetime import timedelta
from cart.models import ShoppingCart
from django.contrib.auth.mixins import LoginRequiredMixin






class OrdersHistoryView(LoginRequiredMixin, View):
    template_name = 'history/orders_history.html'
    
    def get(self, request):
        # محاسبه تاریخ یک ماه پیش
        one_month_ago = timezone.now() - timedelta(days=30)
        
        shopping_carts = ShoppingCart.objects.filter(
            user=request.user,
            is_paid=True,
            paid_at__gte=one_month_ago,
        ).order_by('-paid_at')
        
        context = {
            'shopping_carts': shopping_carts,
        }
        
        return render(request, self.template_name, context)

