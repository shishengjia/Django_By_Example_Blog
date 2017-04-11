from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View
from django.core.mail import send_mail

from .models import Post, Tag
from .forms import EmailPostForm, CommentForm


class PostListView(View):
    """
    博客列表页
    """
    def get(self, request, tag_name=None):
        posts = Post.published.all()
        if tag_name:
            tag = get_object_or_404(Tag, name=tag_name)
            posts = posts.filter(tag__in=[tag])
        return render(request, 'post_list.html', {'posts': posts})


class PostDetailView(View):
    """
    博客详情页
    """
    def get(self, request, year, month, day, post):
        post = get_object_or_404(Post, slug=post, status='published', publish_time__year=year,
                                 publish_time__month=month, publish_time__day=day)

        comments = post.comments.filter(active=True)
        comment_form = CommentForm()

        return render(request, 'post_detail.html', {
            'post': post,
            "comment_form": comment_form,
            "comments": comments
        })

    def post(self, request, year, month, day, post):
        post = get_object_or_404(Post, slug=post, status='published', publish_time__year=year,
                                 publish_time__month=month, publish_time__day=day)

        comments = post.comments.filter(active=True)
        comment_form = CommentForm(data=request.POST)
        new_comment = None
        if comment_form.is_valid():
            # 创建一个实例，但暂时不保存到数据库
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
        return render(request, 'post_detail.html', {
            "post": post,
            "comments": comments,
            "comment_form": comment_form,
            "new_comment": new_comment
        })


class EmailPostView(View):
    """
    发送文章分享邮件
    """
    def get(self, request, post_id):
        post = get_object_or_404(Post, id=post_id, status="published")
        sent = False
        # get请求返回一个空的form进行渲染
        form = EmailPostForm()
        return render(request, 'share.html', {
            "post": post,
            "form": form,
            "sent": sent
        })

    def post(self, request, post_id):
        post = get_object_or_404(Post, id=post_id, status="published")
        sent = False
        form = EmailPostForm(request.POST)
        to = request.POST.get("to", "")
        if form.is_valid():
            cd = form.cleaned_data
            # 构建绝对url
            post_url = request.build_absolute_uri(post.get_absolute_url())
            # 主题
            subject = '{} ({})recommends you reanding "{}"'.format(cd['name'], cd['email'], post.title)
            # 详情
            message = 'Read "{}" at {}\n\n{}\'s comments: {}'.format(post.title, post_url, cd['name'], cd['comments'])
            # 发送
            send_mail(subject, message, '13419516267@sina.cn', [cd['to']])
            sent = True
        return render(request, 'share.html', {
            "post": post,
            "form": form,
            "sent": sent,
            "to": to
        })
