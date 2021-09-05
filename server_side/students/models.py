from django.db import models

# Create your models here.
class Students(models.Model):
    first_name = models.CharField(default='', max_length=200)
    last_name = models.CharField(default='', max_length=200)
    father_name = models.CharField(default='', max_length=200)
    mother_name = models.CharField(default='', max_length=200)
    course_name = models.CharField(verbose_name="students class/standard", default='', max_length=50)
    date_of_birth = models.DateTimeField(verbose_name="date of birth", auto_now=False, auto_now_add=False)
    enrollment_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    address = models.CharField(default='', max_length=200)
