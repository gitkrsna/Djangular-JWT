from django.db import models
from django.contrib.auth.models import User

# Create your models here.
    

class Course(models.Model):
    course_name = models.CharField(max_length=20, default='')
    target_student = models.CharField(max_length=20, default='')
    medium = models.CharField(max_length=20, default='')
    duration = models.CharField(max_length=20, default='')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

class Student(User):
    course = models.ForeignKey(Course, verbose_name= "Course_name", on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    mobile_number = models.CharField(max_length=15)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)


class Post(models.Model):
    author = models.ForeignKey(Student, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    post_image = models.FileField(blank = True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    post= models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_author = models.ForeignKey(Student, on_delete=models.CASCADE)
    comment_content = models.TextField()
    comment_image = models.FileField(blank=True, null=True)
    upvotes = models.IntegerField(default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

class UserUpvote(models.Model):
    user = models.ForeignKey(Student, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
