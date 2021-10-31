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
    def __str__(self):
        return self.course_name

class Student(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, verbose_name= "Course_name", on_delete=models.CASCADE, blank=True, null=True, default='')
    date_of_birth = models.DateField(default='', blank=True, null=True)
    mobile_number = models.CharField(max_length=15, default='', blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.user_id) + " " + "(" + str(self.user.username) + ")" 

class Post(models.Model):
    author = models.ForeignKey(Student, on_delete=models.CASCADE, default='', verbose_name= "Author")
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
