from django.contrib import admin

from .models import Post, Comment, Tag


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish_time', 'status')
    search_fields = ('title', 'body', 'tag')
    # title中的值会被自动填充到slug中
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish_time'
    ordering = ['status', 'publish_time', 'tag']


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')


class TagAdmin(admin.ModelAdmin):
    list_display = ('name', )


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Tag, TagAdmin)
