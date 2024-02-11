from django.contrib import admin
from .models import CustomUser, Book, Category,Transaction, Review

# Register your models here.

# class BookAdmin(admin.ModelAdmin):
#     list_display = (
#         'isbn',
#         'title',
#         'category',
#         'price',
#         'rating',
#         'image',
#     )

#     ordering = ('isbn',)


admin.site.register(Book)
admin.site.register(Category)
admin.site.register(Transaction)
admin.site.register(Review)
