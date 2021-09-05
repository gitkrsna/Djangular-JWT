from django.db import models

Months = [
    ('Jan', 'Freshman'),
    ('Feb', 'Sophomore'),
    ('Mar', 'Junior'),
    ('Apr', 'Senior'),   
    ('May', 'Graduate'),
    ('Jun', 'Graduate'),
    ('Jul', 'Graduate'),
    ('Aug', 'Graduate'),
    ('Sep', 'Graduate'),
    ('Oct', 'Graduate'),
    ('Nov', 'Graduate'),
    ('Dec', 'Graduate'),
]
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

class Fees(models.Model):
    student = models.ForeignKey(Students, default=1, verbose_name="Students", on_delete=models.SET_DEFAULT, primary_key=True)
    fees_month = models.CharField(
        max_length=10,
        choices=Months,
        default= '',
    )
    amount = models.IntegerField(default=0)
