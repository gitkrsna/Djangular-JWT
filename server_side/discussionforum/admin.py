from django.contrib import admin
from .models import Student, Post, Comment, Course, UserUpvote
# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'mobile_number', 'date_of_birth', 'created_on', 'updated_on')

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['course_name', 'target_student', 'medium', 'duration', 'created_on', 'updated_on']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'title', 'content', 'post_image', 'created_on', 'updated_on']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'post', 'comment_author', 'comment_content', 'comment_image', 'upvotes', 'created_on', 'updated_on']

@admin.register(UserUpvote)
class UpvoteAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'comment', 'is_upvote']