from django.shortcuts import render
from rest_framework import mixins
from .models import Post
from .serializer import PostSerializer
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView


# Create your views here.

class post_list(ListCreateAPIView):
    queryset = Post.objects.all().order_by('-uploaded_date')
    serializer_class = PostSerializer

class post_detail(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all().order_by('-uploaded_date')
    serializer_class = PostSerializer