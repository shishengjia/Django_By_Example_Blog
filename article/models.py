# -*- encoding: utf-8 -*-
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class Tag(models.Model):
    """
    标签
    """
    name = models.CharField(max_length=20, verbose_name="标签")

    class Meta:
        verbose_name = "标签"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')


class Post(models.Model):
    """
    文章模型
    """
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )

    title = models.CharField(max_length=250)
    # Django will prevent from multiple posts having the same slug for the same date.
    slug = models.SlugField(max_length=250, unique_for_date='publish_time')
    tag = models.ManyToManyField(Tag)
    author = models.ForeignKey(User, related_name='blog_posts')
    body = models.TextField()
    publish_time = models.DateTimeField(default=timezone.now)
    # auto_now_add here, the date will be saved automatically when creating an object.
    created_time = models.DateTimeField(auto_now_add=True)
    # auto_now here, the date will be updated automatically when saving an object.
    updated_time = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    objects = models.Manager()  # default Manager
    published = PublishedManager()  # custom Manager

    class Meta:
        # sort results by the publish_time field in descending order by default when we query the database.
        ordering = ('-publish_time', )
        verbose_name = "文章"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[
            self.publish_time.year,
            self.publish_time.strftime('%m'),
            self.publish_time.strftime('%d'),
            self.slug])


class Comment(models.Model):
    """
    评论模型
    """
    # 定义related_name属性为comments，可以post.comments.all()访问文章的所有评论，默认是post.comment_set.all()
    post = models.ForeignKey(Post, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.NullBooleanField(default=True)

    class Meta:
        ordering = ('created', )
        verbose_name = "评论"
        verbose_name_plural = verbose_name

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)
