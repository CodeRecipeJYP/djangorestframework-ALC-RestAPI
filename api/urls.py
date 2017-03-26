from django.conf.urls import url
from .views import post_list,post_detail


urlpatterns = [
    url(r'^post/', post_list.as_view()),
    url(r'^post/(?P<pk>[0-9]+)/$', post_detail.as_view()),
]
