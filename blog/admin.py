from django.contrib import admin
from .models import BlogCategory,Blog,BlogComment


# Register your models here.
class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

class BlogAdmin(admin.ModelAdmin):
    list_display = ['title','content','author','pub_time','category']

class BlogCommentAdmin(admin.ModelAdmin):
    list_display = ['content','author','blog','pub_time']

admin.site.register(BlogCategory,BlogCategoryAdmin)
admin.site.register(Blog,BlogAdmin)
admin.site.register(BlogComment,BlogCommentAdmin)