from django.contrib import admin
from .models import CustomUser, Book, Category, Transaction, Review

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'isbn',
        'title',
        'category',
        'price',
        'image',
        )

ordering = ('sku',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Book, BookAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Transaction)
admin.site.register(Review)
