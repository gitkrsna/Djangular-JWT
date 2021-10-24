from rest_framework import serializers
from .models import Student, Course, Post, Comment, UserUpvote

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name','username', 'email', 'mobile_number', 'course', 'date_of_birth', 'created_on', 'updated_on']

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['course_name', 'target_student', 'medium', 'duration', 'created_on', 'updated_on']

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['author', 'title', 'content', 'post_image', 'created_on', 'updated_on']

class CommentSerializer(serializers.Serializer):
    class Meta:
        model = Comment
        fields = ['post', 'comment_author', 'comment_content', 'comment_image', 'upvotes', 'created_on', 'updated_on']

class UserupvoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserUpvote
        fields = ['user', 'comment']