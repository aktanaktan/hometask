from django.shortcuts import render
from rest_framework import permissions
from rest_framework import generics
from blog_api import serializers
from django.contrib.auth.models import User

from blog_api.models import Post, Comment, Category
from blog_api.permissions import IsOwnerOrReadOnly


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer


class PostCreateView(generics.CreateAPIView):
    serializer_class = serializers.PostSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetailView(generics.RetrieveAPIView):
    """Endpoint for Retrieve single post"""
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)


class PostDeleteView(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)


class PostUpdateView(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)


class CategoryView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer

