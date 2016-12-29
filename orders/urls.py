from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    url(r'^$', views.api_root),
    url(r'^posts/$', views.PostList.as_view(), name='post-list'),
    url(r'^posts/(?P<pk>[0-9]+)/$', views.PostDetail.as_view(), name='post-detail'),
    url(r'^comments/$', views.CommentList.as_view(), name='comment-list'),
    url(r'^comments/(?P<pk>[0-9]+)/$', views.CommentDetail.as_view(), name='comment-detail'),
    url(r'^users/$', views.UserList.as_view(), name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='user-detail'),
    url(r'^tags/$', views.TagList.as_view(), name='tag-list'),
    url(r'^tags/(?P<pk>[0-9]+)/$', views.TagDetail.as_view(), name='tag-detail'),
]


urlpatterns = format_suffix_patterns(urlpatterns)


##################################
# urlpatterns = [
#     url(r'^$', views.api_root),
#     url(r'^items/$', views.ItemList.as_view(), name='item-list'),
#     url(r'^items/(?P<pk>[0-9]+)/$', views.ItemDetail.as_view(), name='item-detail'),
#     url(r'^users/$', views.UserList.as_view(), name='user-list'),
#     url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='user-detail'),
# ]
#
#
# urlpatterns = format_suffix_patterns(urlpatterns)