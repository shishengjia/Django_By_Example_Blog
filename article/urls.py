from django.conf.urls import url

from .views import PostDetailView, PostListView

urlpatterns = [
    url(r'^$', PostListView.as_view(), name='post_list'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$', PostDetailView.as_view(),
        name='post_detail')
]