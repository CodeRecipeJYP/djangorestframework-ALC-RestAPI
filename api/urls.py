from django.conf.urls import url
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    url(r'^post/$', post_list.as_view()),
    url(r'^post/(?P<pk>[0-9]+)/$', post_detail.as_view()),

    url(r'^chat/$', chat_list.as_view()),
    url(r'^chat/(?P<pk>[0-9]+)/$', chat_detail.as_view()),

    url(r'^message/$', message_list.as_view()),
    url(r'^message/(?P<pk>[0-9]+)/$', message_detail.as_view()),
]
