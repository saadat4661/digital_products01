from django.contrib import admin

from .models import Product, Category, File
# Register your models here.


class FileInlineAdmin(admin.StackedInline):
    model = File
    fields = ['id', 'title', 'file', 'file_type', 'is_enable']
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_enable', 'created_time']
    list_filter = ['is_enable', 'created_time']
    search_fields = ['title']
    inlines = [FileInlineAdmin]


@admin.register(Category)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['parent', 'title', 'is_enable', 'created_time']
    list_filter = ['is_enable']
    search_fields = ['title']
