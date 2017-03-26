from django.shortcuts import render
from rest_framework import mixins
from .models import Post
from .serializer import PostSerializer
from rest_framework.generics import GenericAPIView


# Create your views here.

class post_api(GenericAPIView, mixins.ListModelMixin):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)