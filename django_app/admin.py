from django.contrib import admin

# Register your models here.
from .models import Post, Book, BookContent
from .forms import PostForm

class PostAdmin(admin.ModelAdmin):
    form = PostForm

admin.site.register(Post, PostAdmin)
admin.site.register(Book)
admin.site.register(BookContent)
