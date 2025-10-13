from django.db import models
from accounts.models import User
from django.core.exceptions import ValidationError


class Address(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='کاربر')
    name = models.CharField(max_length=64, null=True, blank=True)
    email = models.CharField(max_length=128, null=True, blank=True)
    province = models.CharField(max_length=64, verbose_name="استان")
    city = models.CharField(max_length=64, verbose_name="شهر")
    post_code = models.CharField(max_length=10, verbose_name="کد پستی", null=True, blank=True)
    phone_number = models.CharField(max_length=11, verbose_name="شماره تلفن")
    complete_address = models.TextField(max_length=1024, verbose_name="آدرس کامل")
    lng = models.CharField(max_length=32, null=True, blank=True)
    lat = models.CharField(max_length=32, null=True, blank=True)
    
    # فیلدهای زمانی
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="آخرین بروزرسانی")
    
    class Meta:
        verbose_name = "آدرس"
        verbose_name_plural = "آدرس‌ها"
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.name} - {self.phone_number} - {self.city}"
    

    def delete(self, *args, **kwargs):
        # جلوگیری از حذف آدرس
        raise ValidationError("امکان حذف آدرس وجود ندارد. فقط می‌توانید آن را ویرایش کنید.")