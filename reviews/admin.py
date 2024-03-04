from django.contrib import admin
from .models import Review


class ReviewAdmin(admin.ModelAdmin):
    """
    Register the 'Review' model with the admin site
    Filters the reviews
    """
    #list_display = ('book_reviewed', 'reviewer', 'rating', 'date_created')
    #list_filter = ('book_reviewed', 'date_created')
    search_fields = ('reviewer', 'content')
    date_hierarchy = 'date_created'


admin.site.register(Review, ReviewAdmin)
