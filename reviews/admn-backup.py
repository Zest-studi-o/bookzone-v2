from django.contrib import admin
from .models import Review
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Review)
class ReviewAdmin(SummernoteModelAdmin):
    """
    Register the 'Review' model with the admin site
    """

    list_display = ('review_title', 'status', 'date_created')
    search_fields = ['review_title', 'content']
    list_filter = ('status', 'date_created')
    summernote_fields = ('content')