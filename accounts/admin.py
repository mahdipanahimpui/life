from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserCreationForm, UserChangeForm
from .models import User, OtpCode, UserToken, ViewCount
from django.contrib.auth.models import Group

class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm


    list_display = ('phone_number', 'is_admin', 'last_login')
    list_filter = ('is_admin',)



    fieldsets = (
        (None, {'fields': ('phone_number', 'password')}),
        ('permissions', {'fields': ('is_active', 'is_admin', 'last_login')}),
    )


    add_fieldsets = (
        (None, {'fields': ('phone_number',)}),
    )


    search_fields = ('phone_number',)
    ordering = ('last_login',)
    filter_horizontal = ()



# ------------------------------------------
@admin.register(OtpCode)
class OtpCodeAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'code', 'created_at')

# ------------------------------------------
@admin.register(UserToken)
class UserTokenAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at', 'expires_at', 'refresh_token')

# ----------------------------------------------
admin.site.unregister(Group)
admin.site.register(User, UserAdmin)



# -------------------------------------------------------4
@admin.register(ViewCount)
class ViewCountAdmin(admin.ModelAdmin):
    list_display = ['view_name', 'slug', 'user', 'count', 'last_visited', 
                    'get_total_by_slug', 'get_total_by_view', 'get_total_by_url'
    ]
    list_filter = ['view_name', 'slug']
    search_fields = ['view_name', 'slug', 'user__phone_number', 'url']
    readonly_fields = ['url']
    list_per_page = 20
    
    def get_total_by_slug(self, obj):
        """جمع کل بازدیدها برای اسلاگ این رکورد"""
        if obj.slug:
            return ViewCount.get_total_views_by_slug(obj.slug)
        return 0
    
    def get_total_by_view(self, obj):
        """جمع کل بازدیدها برای نام ویو این رکورد"""
        return ViewCount.get_total_views_by_view_name(obj.view_name)
    
    def get_total_by_url(self, obj):
        """جمع کل بازدیدها برای الگوی URL این رکورد"""
        if obj.url:
            # استخراج بخش اصلی URL (بدون پارامترهای کوئری)
            url_pattern = obj.url.split('?')[0]
            return ViewCount.get_total_views_by_url_pattern(url_pattern)
        return 0
   
    def get_queryset(self, request):
        """بهینه‌سازی کوئری برای جلوگیری از N+1"""
        return super().get_queryset(request).select_related('user')
    
    # اضافه کردن action برای ادمین
    actions = ['reset_counts']
    
    def reset_counts(self, request, queryset):
        """ریست کردن تعداد بازدیدهای انتخاب شده"""
        updated = queryset.update(count=0)
        self.message_user(request, f'{updated} رکورد با موفقیت ریست شد.')
