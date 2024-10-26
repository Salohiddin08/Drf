from django.contrib import admin
from .models import Category, Product, Order, User

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')
    search_fields = ('name',)
    ordering = ('-created_at',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'price', 'quantity', 'created_at', 'updated_at')
    list_filter = ('category',)
    search_fields = ('name',)
    ordering = ('-created_at',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'total_price', 'quantity', 'created_at', 'updated_at')
    list_filter = ('user',)
    search_fields = ('user__username',)  
    ordering = ('-created_at',)

    