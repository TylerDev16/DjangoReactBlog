from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import BlogPost, Category


# Apply summernote to all TextField in model.
class BlogPostAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    exclude = ('slug',)
    list_display = ('title', 'category', 'created_at', 'updated_at')
    list_display_links = ('title',)
    search_fields = ('title', 'content')
    list_per_page = 10
    summernote_fields = '__all__'

class CategoryAdmin(admin.ModelAdmin):
    exclude = ('slug',)

admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Category, CategoryAdmin)
