from django.contrib import admin
from .models import Review


class ReviewAdmin(admin.ModelAdmin):
    """
    Allows the admin to edit reviews in the admin panel
    & also to filter them
    """
    list_display = ('book', 'reviewer', 'rating', 'date_created')
    list_filter = ('book', 'date_created')
    search_fields = ('reviewer', 'content')
    date_hierarchy = 'date_created'


admin.site.register(Review, ReviewAdmin)
