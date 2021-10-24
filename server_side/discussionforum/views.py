from .serializers import UserupvoteSerializer, CommentSerializer, PostSerializer, CourseSerializer, StudentSerializer
from .models import Student, Course, Post, Comment, UserUpvote
from students.ContextViewSet import ViewSet
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