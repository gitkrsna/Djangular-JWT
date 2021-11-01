from rest_framework import serializers
from .models import Student, Course, Post, Comment, UserUpvote
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'username' , 'password', 'is_active', 'is_superuser', 'is_staff')
class StudentCreateSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Student
        fields = [ 'user', 'mobile_number', 'course', 'date_of_birth', 'created_on', 'updated_on']
    def create(self, validated_data):
        user = validated_data.pop('user') 
        user_instance = User.objects.create(**user) 
        return Student.objects.create(user=user_instance , **validated_data)

class StudentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = [ 'user', 'mobile_number', 'course', 'date_of_birth', 'created_on', 'updated_on']


class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Student
        fields = [ 'user', 'mobile_number', 'course', 'date_of_birth', 'created_on', 'updated_on']

class CourseSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Course
        fields = ['course_name', 'target_student', 'medium', 'duration', 'created_on', 'updated_on']

#author is foreign key in post model, so only pass author id instead of author object
class PostSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Post 
        fields = ['author', 'title', 'content', 'post_image', 'created_on', 'updated_on']


# this serializer is used to serialize the post data and is example of nested serializer
# in this modal we will pass author object instead of author id
class PostSerializerWithNestedField(serializers.ModelSerializer):
    author = StudentSerializer() # author is a foreign key
    class Meta: # Meta class is used to specify additional options for the serializer
        model = Post # Specifies the model that the serializer serializes
        fields = ['author', 'title', 'content', 'post_image', 'created_on', 'updated_on'] # Specifies the fields that should be serialized
    # customized create method will first save author and then save post
    def create(self, validated_data):
        author = validated_data.pop('author') # pop() removes the author key from validated_data
        author_instance = Student.objects.create(**author) # create() creates a new instance of the author model
        return Post.objects.create(author=author_instance , **validated_data)   # create() creates a new instance of the post model
        # **validated_data is used to create a new instance of the post model with the validated data
        # validated_data is a dictionary of the validated data  

class CommentSerializer(serializers.Serializer):

    class Meta:
        model = Comment
        fields = ['post', 'comment_author', 'comment_content', 'comment_image', 'upvotes', 'created_on', 'updated_on']

class UserupvoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserUpvote
        fields = ['user', 'comment']


# only for author info that will be displayed in the post detail page
class AuthorInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = [ 'mobile_number', 'date_of_birth']

class PostListSerializer(serializers.ModelSerializer):
    author = AuthorInfoSerializer()
    class Meta:
        model = Post
        fields = ['author', 'title', 'content', 'post_image']
class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['author', 'title', 'content', 'post_image']       
