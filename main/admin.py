from django.contrib import admin
from .models import Product
from .models import Phone

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'is_active', 'created_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('name', 'description')
    list_editable = ('price', 'is_active')
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ('created_at',)

@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'price_usd_display')
    readonly_fields = ('price_usd_display',)

    fields = ('name', 'description', 'price', 'price_usd_display', 'image')

# Register your models here.
