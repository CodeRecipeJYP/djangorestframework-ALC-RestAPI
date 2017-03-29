from django.shortcuts import render
from rest_framework import mixins
from .models import Post, Chat, Message
from .serializer import PostSerializer, ChatSerializer, MessageSerializer
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView


# Create your views here.

class post_list(ListCreateAPIView):
    queryset = Post.objects.all().order_by('-uploaded_date')
    serializer_class = PostSerializer

class post_detail(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all().order_by('-uploaded_date')
    serializer_class = PostSerializer


class chat_list(ListCreateAPIView):
    queryset = Chat.objects.all().order_by('-created_date')
    serializer_class = ChatSerializer

class chat_detail(RetrieveUpdateDestroyAPIView):
    queryset = Chat.objects.all().order_by('-created_date')
    serializer_class = ChatSerializer



class message_list(ListCreateAPIView):
    queryset = Message.objects.all().order_by('-created_date')
    serializer_class = MessageSerializer

class message_detail(RetrieveUpdateDestroyAPIView):
    queryset = Message.objects.all().order_by('-created_date')
    serializer_class = MessageSerializer