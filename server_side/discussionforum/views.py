from django.views.generic.base import RedirectView

from .serializers import PostCreateSerializer, PostListSerializer, UserupvoteSerializer, CommentSerializer, PostSerializer, CourseSerializer, StudentSerializer
from .models import Student, Course, Post, Comment, UserUpvote
from students.ContextViewSet import ViewSet, CreateView, UpdateView, DeleteView, ListView, DetailView
from rest_framework import mixins, reverse, status 
from rest_framework.response import Response
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
        print("request user id is", self.request.user.id)
        print("request username is", self.request.user.username)
        print("request user password is", self.request.user.password)
        return Post.objects.filter() 



class PostCreateView(CreateView):
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer

class PostUpdateOrDeleteView(UpdateView, DeleteView):
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer

class PostDetailView(DetailView):
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer
