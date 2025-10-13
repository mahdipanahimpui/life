from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import UserManager
from datetime import timedelta
from django.utils import timezone
import random, string


class User(AbstractBaseUser):
    phone_number = models.CharField(max_length=11, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    objects = UserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []


    def __str__(self):
        return self.phone_number
    

    def has_perm(self, perm, obj=None):
        return True
    
    def has_perms(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
    

    @property
    def is_staff(self):
        return self.is_admin
    
    


# -------------------------------------------
class OtpCode(models.Model):
    phone_number = models.CharField(max_length=11)
    code = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now=True)
    is_used = models.BooleanField(default=False)

    def is_valid(self):
        return not self.is_used and (timezone.now() - self.created_at) < timedelta(minutes=5)
    
    def mark_as_used(self):
        self.is_used = True
        self.save()

    def __str__(self):
        return f'{self.phone_number} - {self.code} - {self.created_at} '

    


class UserToken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='devices')
    refresh_token = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()
    
    def is_valid(self):
        return timezone.now() < self.expires_at
    
    @classmethod
    def generate_refresh_token(cls):
        return ''.join(random.choices(string.ascii_letters + string.digits, k=64))
    



# -------------------------------------------------------------------------------

class ViewCount(models.Model):
    view_name = models.CharField(max_length=255,)
    url = models.CharField(max_length=500,)  # جدید
    slug = models.CharField(max_length=200, blank=True, null=True)  # جدید
    user = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
    )
    count = models.PositiveIntegerField(default=0)
    last_visited = models.DateTimeField(auto_now=True)


    @classmethod
    def get_total_views_by_slug(cls, slug):
        """جمع کل بازدیدها برای یک اسلاگ خاص"""
        return cls.objects.filter(slug=slug).aggregate(
            total_views=models.Sum('count')
        )['total_views'] or 0
    
    @classmethod
    def get_total_views_by_view_name(cls, view_name):
        """جمع کل بازدیدها برای یک ویو خاص"""
        return cls.objects.filter(view_name=view_name).aggregate(
            total_views=models.Sum('count')
        )['total_views'] or 0
    
    @classmethod
    def get_total_views_by_url_pattern(cls, url_pattern):
        """جمع کل بازدیدها برای URLهای مشابه"""
        return cls.objects.filter(url__icontains=url_pattern).aggregate(
            total_views=models.Sum('count')
        )['total_views'] or 0
    
    class Meta:
        unique_together = ['view_name', 'user', 'slug']  # به‌روزرسانی شده
    
    def __str__(self):
        phone_number = self.user.phone_number if self.user else "Anonymous"
        return f"{self.view_name} - {self.slug} - {phone_number}"