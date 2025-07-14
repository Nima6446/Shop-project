from django.contrib import admin
from . import models
from .models import ProductVisit, ProductGallery


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        "slug": ["title"]
    }
    list_display = ["title","price","is_active","is_delete"]
    list_filter = ["category","is_active"]
    search_fields = ["title"]
    list_editable = ["price","is_active"]

admin.site.register(models.product,ProductAdmin)
admin.site.register(models.category)
admin.site.register(models.products_tags)
admin.site.register(models.product_brand)
admin.site.register(ProductVisit)
admin.site.register(ProductGallery)