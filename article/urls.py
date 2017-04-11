from django.conf.urls import url

from .views import PostDetailView, PostListView, EmailPostView

urlpatterns = [
    url(r'^$', PostListView.as_view(), name='post_list'),
    url(r'^tag/(?P<tag_name>[-+\w]+)/$', PostListView.as_view(), name='post_list_by_tag'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$', PostDetailView.as_view(),
        name='post_detail'),
    url(r'^(?P<post_id>\d+)/share/$', EmailPostView.as_view(), name="post_share")
]