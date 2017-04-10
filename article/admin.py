from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish_time', 'status')
    search_fields = ('title', 'body')
    # title中的值会被自动填充到slug中
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish_time'
    ordering = ['status', 'publish_time']

admin.site.register(Post, PostAdmin)