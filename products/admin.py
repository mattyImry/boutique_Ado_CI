from django.contrib import admin
from .models import Product, Category

# Register your models here.

# here we create this 2 classes to be able to display the product and cat.
# you can change the order of columns in admin here


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

# sorting product by sku if you put '-sku' invert the sorting
    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
