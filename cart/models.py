from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from accounts.models import User


class DeliveryOption(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=256)
    price = models.IntegerField()

    def __str__(self):
        return f'{self.title} - {self.price}'
    
class PaymentOption(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=256)
    code = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return f'{self.title}'


class ShoppingCart(models.Model):
    delivery_option = models.ForeignKey(DeliveryOption, on_delete=models.SET_NULL, null=True, blank=True)
    payment_option = models.ForeignKey(PaymentOption, on_delete=models.SET_NULL, null=True, blank=True)
    total_product_price = models.PositiveIntegerField(null=True, blank=True)
    delivery_price = models.PositiveIntegerField(null=True, blank=True)
    price_to_pay = models.PositiveIntegerField(null=True, blank=True)
    paid_price = models.PositiveIntegerField(null=True, blank=True)
    ref_code = models.CharField(max_length=256, null=True, blank=True)
    paid_at = models.DateTimeField(null=True, blank=True)
    is_paid = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    card_number = models.CharField(max_length=19, null=True, blank=True)
    status = models.CharField(max_length=64, default='در حال پردازش')

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user'],
                condition=models.Q(is_paid=False),
                name='unique_unpaid_cart_per_user'
            )
        ]

    def save(self, *args, **kwargs):
        # اگر cart جدید است و کاربر دارد، بررسی کن که cart پرداخت نشده دیگری نداشته باشد
        if self.pk is None and self.user and not self.is_paid:
            existing_unpaid = ShoppingCart.objects.filter(user=self.user, is_paid=False).exists()
            if existing_unpaid:
                raise ValidationError("این کاربر قبلاً یک سبد خرید پرداخت نشده دارد.")
        
        if self.is_paid and self.paid_at is None:
            self.paid_at = timezone.now()
        
        if not self.is_paid and self.paid_at is not None:
            self.paid_at = None
        
        super().save(*args, **kwargs)

    def get_or_create_unpaid_cart(user):
        """تابع کمکی برای دریافت یا ایجاد سبد خرید پرداخت نشده"""
        cart, created = ShoppingCart.objects.get_or_create(
            user=user,
            is_paid=False,
            defaults={'user': user}
        )
        return cart
    

    def __str__(self):
        return f"Cart:{self.id} - User:{self.user} - Paid:{self.is_paid} - at:{self.paid_at}"