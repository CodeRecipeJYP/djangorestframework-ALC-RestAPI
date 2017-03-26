from django.shortcuts import render
from rest_framework import mixins
from .models import Post
from .serializer import PostSerializer
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView


# Create your views here.

class post_list(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    #
    # def get(self, request, *args, **kwargs):
    #     return self.list(request, *args, **kwargs)
    #
    # def post(self, request, *args, **kwargs):
    #     return self.create(request, *args, **kwargs)

class post_detail(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    #
    # def get(self, request, *args, **kwargs):
    #     return self.retrieve(request, *args, **kwargs)
    #
    # def put(self, request, *args, **kwargs):
    #     return self.update(request, *args, **kwargs)
    #
    # def delete(self, request, *args, **kwargs):
    #     return self.destroy(request, *args, **kwargs)