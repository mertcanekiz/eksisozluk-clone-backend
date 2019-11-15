from django.shortcuts import render
from rest_framework import viewsets, generics, permissions, renderers, viewsets

from .models import Post, Thread
from django.contrib.auth.models import User

from .serializers import PostSerializer, ThreadSerializer, UserSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class ThreadViewSet(viewsets.ModelViewSet):
    queryset = Thread.objects.all()
    serializer_class = ThreadSerializer

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
