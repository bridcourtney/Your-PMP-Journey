from django.contrib import admin
from .models import Product, Category, ProductReview, DatesAvailable

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'book_type',
        'price',
        'image',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class ProductReviewAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'user',
        'created',
        'image',
    )

    ordering = ('product',)


class DatesAvailableAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'date_available',
    )

    ordering = ('product',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ProductReview, ProductReviewAdmin)
admin.site.register(DatesAvailable, DatesAvailableAdmin)
