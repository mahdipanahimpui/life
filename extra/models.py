from django.db import models

class Notification(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان")
    message = models.TextField(verbose_name="متن اطلاعیه")
    is_active = models.BooleanField(default=True, verbose_name="فعال")
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    