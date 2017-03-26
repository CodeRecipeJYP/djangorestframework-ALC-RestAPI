from django.conf.urls import url
from .views import post_api


urlpatterns = [
    url(r'^post/', post_api.as_view()),
    ]
