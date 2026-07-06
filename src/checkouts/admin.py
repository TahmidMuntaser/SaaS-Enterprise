from django.contrib import admin

from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "created_at", "updated_at"]
    search_fields = ["name"]


admin.site.register(Product, ProductAdmin)
