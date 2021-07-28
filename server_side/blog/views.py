from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets, permissions
from .models import BlogPost
from . import serializers


class UserViewSet(viewsets.ModelViewSet):
    """
    Provides basic CRUD functions for the User model
    """
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class BlogPostViewSet(viewsets.ModelViewSet):
    """
    Provides basic CRUD functions for the Blog Post model
    """
    queryset = BlogPost.objects.all()
    serializer_class = serializers.BlogPostSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)