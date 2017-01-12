from django.contrib import admin

from .models import Post

class PostAdmin(admin.ModelAdmin):
    """ posts.slug is auto-generated so we will remove it from the form """
    exclude = ('slug',)

admin.site.register(Post, PostAdmin)
