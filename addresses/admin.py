from django.contrib import admin
from .models import Address

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'city', 'province', 'lat', 'lng', 'phone_number', 'email', 'complete_address', 'created_at']
    search_fields = ['province', 'city', 'phone_number', 'complete_address']
    list_filter = ['province', 'city']