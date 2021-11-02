import re
from django.contrib.auth.models import User
from django.http.request import QueryDict
from django.views.generic.base import RedirectView
from django.http import JsonResponse

from .serializers import PostCreateSerializer, PostListSerializer, PostWithCommentSerializer, StudentCreateSerializer, StudentUpdateSerializer, UserupvoteSerializer, CommentSerializer, PostSerializer, CourseSerializer, StudentSerializer
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

class StudentCreateView(CreateView):
    def create(self, request, *args, **kwargs):
        if not request.data:
            raise NotAcceptable(detail="No data provided")
        if 'user' not in request.data:
            raise NotAcceptable(detail="No User data provided") 
        if 'email' not in request.data['user']:
            raise NotAcceptable(detail="No email provided")       
  
        if 'password1' not in request.data['user']:
            raise NotAcceptable(detail="No password1 provided") 
        if 'password2' not in request.data['user']:
            raise NotAcceptable(detail="No password2 provided")      
        #check both passwords are same
        password1 =  request.data['user']['password1']
        password2 = request.data['user']['password2']
        if password1 != password2:
            raise ValidationError({'detail': 'Passwords do not match'})
        else:
            request.data['user']['password'] = password1
            request.data['user']['username'] = request.data['user']['email']
            request.data['date_of_birth'] = None
            # request.data['user']['is_staff'] = True
            # request.data['user']['is_superuser'] = True
            # request.data['user']['is_active'] = True
            del request.data['user']['password1']
            del request.data['user']['password2']
        # call parent create method after modifying request data
        return super().create(request, *args, **kwargs)
    queryset = Student.objects.all()
    serializer_class = StudentCreateSerializer

class StudentUpdateView(UpdateView):
    def update(self, request, *args, **kwargs):
        if int(kwargs.get('pk')) != self.request.user.id:
            raise NotAcceptable(detail="You are not authorized for this action")
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)
    def get_queryset(self):
        return Student.objects.filter(user__id=self.request.user.id)
    serializer_class = StudentUpdateSerializer

class CourseViewSet(ViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer   

class PostViewSet(ViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer 

class PostWithCommentViewSet(ViewSet):     
    def get_queryset(self):
        return Post.objects.filter(id=self.kwargs['pk']).select_related('author').prefetch_related('comment')
    serializer_class = PostWithCommentSerializer

class UserUpvoteViewSet(ViewSet):
    queryset = UserUpvote.objects.all()
    serializer_class = UserupvoteSerializer         




class PostListView(ListView):
    serializer_class = PostWithCommentSerializer
    def get_queryset(self): # get_queryset is used to customize the queryset
        # print("request user id is", self.request.user.id)
        # print("request username is", self.request.user.username)
        # print("request user password is", self.request.user.password)
        return Post.objects.all().select_related('author').prefetch_related('comment')



class PostCreateView(CreateView):
     # modify create method to add author to the post
    def create(self, request, *args, **kwargs):
        # modify request data to add author to the post
        request.data.pop('author', None)
        request.data['author'] = self.request.user.id
        # check if request user is an student
        user_exist = Student.objects.filter(user=self.request.user).exists()
        if not user_exist:
            raise PermissionDenied("You are not a student/author")
        post_title_exist = Post.objects.filter(title=request.data['title']).exists()
        if post_title_exist:
            raise ValidationError({'details': 'Title already exist.'}) 
            
        # call parent create method after modifying request data
        return super().create(request, *args, **kwargs)
    def get_queryset(self):
        return Post.objects.filter(author_id=self.request.user.id)
    serializer_class = PostCreateSerializer

class PostUpdateDeleteView(UpdateView, DeleteView):
    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
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
        # user_exist = Student.objects.filter(user=self.request.user).exists()
        # if not user_exist:
        #     raise PermissionDenied("You are not a student/author")
        # object_exist = Post.objects.filter(id=self.kwargs['pk']).exists()
        # if not object_exist:
        #     raise NotFound(detail="Error 404, Id Not Found", code=404)   
        return super().destroy(request, *args, **kwargs)
    
    def get_queryset(self):
        return Post.objects.filter(author_id=self.request.user.id)
    serializer_class = PostCreateSerializer

class PostDetailView(DetailView):
    def get_queryset(self):
        return Post.objects.filter(id=self.kwargs['pk'])
    serializer_class = PostCreateSerializer
