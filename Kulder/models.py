from django.db import models
from django_countries.fields import CountryField
from django.contrib.auth.models import User
# pip install django_countries


# Create your models here.
class Lesson(models.Model):
    # days_of_the_week          = (('Monday', 'Monday'),
    #                             ('Tuesday', 'Tuesday'),
    #                             ('Wednesday', 'Wednesday'),
    #                             ('Thursday', 'Thursday'),
    #                             ('Friday', 'Friday'),
    #                             ('Saturday', 'Saturday'),
    #                             ('Sunday', 'Sunday'))

    name                       = models.CharField(max_length = 128)
    slug                       = models.SlugField(allow_unicode=True)
    range                      = models.CharField(max_length=64, blank=True, null=True)
    description                = models.TextField()
    image                      = models.ImageField(upload_to='lesson/', blank=True, null=True)
    days                       = models.CharField(max_length=32, blank=True, null=True)
    # days                       = models.CharField(max_length=32, blank=True, null=True, choices = days_of_the_week)
    lessen_start_time          = models.DateTimeField(auto_now_add=False)
    lesson_end_time            = models.DateTimeField(auto_now_add=False)

    def __str__(self):
        return self.name





class Executive(models.Model):
    user                         = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    name                         = models.CharField(max_length=128)
    slug                         = models.SlugField(allow_unicode=True)
    email                        = models.EmailField(blank=True, null=True)
    phone                        = models.CharField(max_length=20, null=True, blank=True)
    profession                   = models.CharField(max_length=128, blank=True, null=True)
    possition                    = models.CharField(max_length=128)
    about                        = models.TextField()
    profile_pic                  = models.ImageField(upload_to='employee/', blank=True, null=True)
    nationality                  = CountryField()
    address                      = models.CharField(max_length=256, blank=True, null=True)
    experience                   = models.TextField()




    def __str__(self):
        return self.name












class Support_for_Students(models.Model):
    kind_of_choice              = (
                                  ('Support for students with family', 'Support for students with family'),
                                  ('Support for Dormitory-based students', 'Support for Dormitory-based students'),
                                  ('support for home-based students', 'support for home-based students')
                                 )


    title                       = models.CharField(max_length=128)
    slug                        = models.SlugField(allow_unicode=True)
    description                 = models.TextField()
    kind_of_support             = models.CharField(max_length=128, choices=kind_of_choice, blank=True, null=True)
    image                       = models.ImageField(upload_to='Support_for_Students/', blank=True, null=True)


    def __str__(self):
        return self.title










class AboutUs(models.Model):
    goals                        = models.TextField()
    adress                       = models.CharField(max_length=256, blank=True, null=True)
    name                         = models.CharField(max_length=64, null=True, blank=True)
    tel1                         = models.CharField(max_length=16, null=True, blank=True)
    tel2                         = models.CharField(max_length=16, null=True, blank=True)
    email                        = models.EmailField(null=True, blank=True)
    aboutus                      = models.TextField()
    comments                     = models.TextField()

    def __str__(self):
        return self.name





class Contact(models.Model):
    name                         = models.CharField(max_length=64, blank=True, null=True)
    surname                      = models.CharField(max_length=64, blank=True, null=True)
    tel                          = models.CharField(max_length=16,null=True,blank=True)
    email                        = models.EmailField(null=True, blank=True)
    subject                      = models.CharField(max_length=256)
    description                  = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.name)









class Student(models.Model):
    gender_choice = (('Male', 'Male'), ('Female', 'Female'))

    residence_choice = (('Dormitory', 'Dormitory'), ('Home', 'Home'))

    class_choice = (('1', 'First year'),
                    ('2', 'Second year'),
                    ('3', 'Third year'),
                    ('4', 'Fouth year'),
                    ('5', 'Fifth year'),
                    ('6', 'Sixth year'))

    level_of_education = (('Undergraduate', 'Undergraduate'),
                          ('Masters', 'Masters'),
                          ('Doctorate', 'Phd'))

    user                         = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name                         = models.CharField(max_length=200)
    slug                         = models.SlugField(unique=True, allow_unicode=True)
    studentID                    = models.IntegerField()
    _class                       = models.CharField(max_length=15, choices=class_choice)
    email                        = models.EmailField(blank=True, null=True)
    phone                        = models.CharField(max_length=20, blank=True, null=True)
    gender                       = models.CharField(max_length=20, choices=gender_choice)
    profile_pic                  = models.ImageField(upload_to='profile_pictures', null=True, blank=True)
    nationality                  = CountryField()
    about                        = models.TextField(null=True, blank=True)
    residence_type               = models.CharField(max_length=30, choices=residence_choice)
    dormitory                    = models.CharField(max_length=300, null=True, blank=True, help_text='if applicable')
    address                      = models.CharField(max_length=450, null=True, blank=True)
    university                   = models.CharField(max_length=150, default='KTÜ')
    department                   = models.CharField(max_length=250)
    degree_level                 = models.CharField(max_length=100, choices=level_of_education)
    graduate                     = models.BooleanField(default=False)
    date_graduated               = models.DateTimeField(auto_now=False, null=True, blank=True, help_text="if applicable")
    profession                   = models.CharField(max_length=150, default='Student', null=True, blank=True)

    def _str_(self):
        return self.name



class Activity(models.Model):
    title                        = models.CharField(max_length=250)
    slug                         = models.SlugField(allow_unicode=True, unique=True)
    description                  = models.TextField(null=True, blank=True)
    image                        = models.ImageField(upload_to='activities', blank=True, null=True)
    date_of_activity             = models.DateTimeField(auto_now=False)
    location                     = models.CharField(max_length=200)
    participants                 = models.ManyToManyField(Student, blank=True)

    def _str_(self):
        return self.title


