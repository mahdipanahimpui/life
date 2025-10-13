from .models import ShoppingCart  # یا مدل مربوط به سبد خرید

def cart_item_count(request):
    item_count = 0
    if request.user.is_authenticated:
        shopping_cart = ShoppingCart.objects.filter(user=request.user, is_paid=False).first()
        if shopping_cart:
            invoice_orders = shopping_cart.invoice_orders.all().count()
            flyer_orders = shopping_cart.flyer_orders.all().count()
            prescription_orders = shopping_cart.prescription_orders.all().count()
            item_count = invoice_orders + flyer_orders + prescription_orders

    return {'item_count': item_count}