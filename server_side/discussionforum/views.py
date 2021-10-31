import re
from django.contrib.auth.models import User
from django.http.request import QueryDict
from django.views.generic.base import RedirectView
from django.http import JsonResponse

from .serializers import PostCreateSerializer, PostListSerializer, UserupvoteSerializer, CommentSerializer, PostSerializer, CourseSerializer, StudentSerializer
from .models import Student, Course, Post, Comment, UserUpvote
from students.ContextViewSet import ViewSet, CreateView, UpdateView, DeleteView, ListView, DetailView
from rest_framework import mixins, reverse, status, viewsets 
from rest_framework.response import Response
from rest_framework.exceptions import APIException, NotAcceptable, NotFound, PermissionDenied, ValidationError
from rest_framework import status
# Create your views here.
class StudentViewSet(ViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
class CourseViewSet(ViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer   

class PostViewSet(ViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer 

class CommentViewSet(ViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer     

class UserUpvoteViewSet(ViewSet):
    queryset = UserUpvote.objects.all()
    serializer_class = UserupvoteSerializer         




class PostListView(ListView):
    serializer_class = PostListSerializer
    def get_queryset(self): # get_queryset is used to customize the queryset
        # print("request user id is", self.request.user.id)
        # print("request username is", self.request.user.username)
        # print("request user password is", self.request.user.password)
        return Post.objects.all() 



class PostCreateView(CreateView):
     # modify create method to add author to the post
    def create(self, request, *args, **kwargs):
        # modify request data to add author to the post
        request.data.pop('author', None)
        request.data['author'] = self.request.user.id
        # check if request user is an student
        user_exist = Student.objects.filter(user=self.request.user).exists()
        print("user count is", user_exist)
        if not user_exist:
            raise PermissionDenied("You are not a student/author")
        post_title_exist = Post.objects.filter(title=request.data['title']).exists()
        if post_title_exist:
            raise ValidationError({'details': 'Title already exist.'}) 
            
        # call parent create method after modifying request data
        return super().create(request, *args, **kwargs)
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer

class PostUpdateDeleteView(UpdateView, DeleteView):
    def update(self, request, *args, **kwargs):
        # check if request user is an student
        user_exist = Student.objects.filter(user=self.request.user).exists()
        if not user_exist:
            raise PermissionDenied("You are not a student/author")

        object_exist = Post.objects.filter(id=self.kwargs['pk']).exists()
        if not object_exist:
            raise NotFound(detail="Error 404, ID Not Found", code=404)     

        post_title_exist = Post.objects.filter(title=request.data['title']).exists()
        if post_title_exist:
            raise ValidationError({'details': 'Title already exist.'}) 
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        # check if request user is an student
        user_exist = Student.objects.filter(user=self.request.user).exists()
        if not user_exist:
            raise PermissionDenied("You are not a student/author")
        object_exist = Post.objects.filter(id=self.kwargs['pk']).exists()
        if not object_exist:
            raise NotFound(detail="Error 404, Id Not Found", code=404)   
        return super().destroy(request, *args, **kwargs)
    
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer

class PostDetailView(DetailView):
    def get_queryset(self):
        return Post.objects.filter(id=self.kwargs['pk'])
    serializer_class = PostCreateSerializer
