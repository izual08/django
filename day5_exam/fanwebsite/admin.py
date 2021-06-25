from django.contrib import admin
from .models import Post

admin.site.site_header = "Fan Website"
admin.site.site_title  = "Fan Website Admin Area"
admin.site.index_title = "Welcome to the Fan Website Admin"

class PostAdmin(admin.ModelAdmin):
    pass

admin.site.register(Post, PostAdmin)
