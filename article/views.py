from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View

from .models import Post


class PostListView(View):
    def get(self, request):
        posts = Post.published.all()
        return render(request, 'post_list.html', {'posts': posts})


class PostDetailView(View):
    def get(self, request, year, month, day, post):
        post = get_object_or_404(Post, slug=post, status='published', publish_time__year=year,
                                 publish_time__month=month, publish_time__day=day)
        return render(request, 'post_detail.html', {'post': post})
