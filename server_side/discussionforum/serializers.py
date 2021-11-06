from rest_framework import serializers
from .models import Student, Course, Post, Comment, UserUpvote
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'username', 'first_name', 'last_name', 'password', 'is_active', 'is_superuser', 'is_staff')
class StudentCreateSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Student
        fields = [ 'user', 'mobile_number', 'course', 'date_of_birth', 'created_on', 'updated_on']
    def create(self, validated_data):
        user = validated_data.pop('user') 
        # use create_user method of User model to create a new user
        user_instance = User.objects.create_user(**user)  # **user is used to unpack the dictionary 
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

class UpvoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserUpvote
        fields = ['user']
class CommentSerializer(serializers.ModelSerializer):
    userupvote = UpvoteSerializer(many=True)
    class Meta:
        model = Comment
        fields = ['comment_content', 'userupvote', 'upvotes', 'created_on', 'updated_on']

class PostWithCommentSerializer(serializers.ModelSerializer):
    comment = CommentSerializer(many=True)
    class Meta:
        model = Post
        fields = ['title', 'content', 'post_image', 'created_on', 'updated_on', 'comment']

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
    comment = CommentSerializer(many=True)
    class Meta:
        model = Post
        # fields you want to send/display to the client
        fields = ['author', 'title', 'content', 'post_image', 'comment']
class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        # fields you want to save in the database
        fields = ['author', 'title', 'content', 'post_image']       

class UpvoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserUpvote
        fields = ['user', 'comment', 'is_upvote']

    def create(self, validated_data):
        comment_id = validated_data.pop('comment')
        comment_instance = Comment.objects.get(id=comment_id)
        if validated_data.get('is_upvote') == True:
            comment_instance.upvotes += 1
            comment_instance.save()
        return UserUpvote.objects.create(comment=comment_instance, **validated_data)

    def update(self, instance, validated_data):
        if validated_data.get('is_upvote') == False and instance.is_upvote == True: 
            instance.comment.upvotes -= 1
            instance.comment.save()
        elif validated_data.get('is_upvote') == True and instance.is_upvote == False:
            instance.comment.upvotes += 1
            instance.comment.save() 
        instance.is_upvote = validated_data.get('is_upvote')
        instance.save()
        return instance    
        