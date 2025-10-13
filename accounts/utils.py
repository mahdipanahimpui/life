# utils.py
from functools import wraps
from .models import ViewCount

def count_view(view_name):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            # جلوگیری از ثبت بازدید برای ادمین و استاف
            if request.user.is_authenticated:
                if request.user.is_superuser or request.user.is_staff:
                    return view_func(request, *args, **kwargs)
            
            # دریافت اسلاگ از آرگومان‌ها
            slug = kwargs.get('slug', '')
            
            # ساخت URL کامل
            full_url = request.build_absolute_uri()
            
            # ثبت بازدید با اسلاگ و URL
            user = request.user if request.user.is_authenticated else None
            view_count, created = ViewCount.objects.get_or_create(
                view_name=view_name,
                user=user,
                slug=slug,
                defaults={'url': full_url}
            )
            
            # اگر رکورد وجود داشت، URL را به‌روزرسانی کن
            if not created:
                view_count.url = full_url
            
            view_count.count += 1
            view_count.save()
            
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator