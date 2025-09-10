from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    experience_count = models.IntegerField(default=0) 
    project_count = models.IntegerField(default=0)
    position = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=12)
    about_me = models.TextField(null=True , max_length=10000)
    facebook = models.URLField(null=True)
    twitter = models.URLField(null=True)
    google_plus = models.URLField(null=True)
    linkedin = models.URLField(null=True)
    github = models.URLField(null=True)
    
    
    
class Experience(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    title  = models.CharField(null=True , max_length=50)
    description = models.TextField(null=True , max_length=200)
    employer = models.CharField(null=True , max_length=50)
    employee_start_date = models.DateField(null=True)
    employee_end_date = models.DateField(null=True)
    
    
    
class Skill(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    title = models.CharField(null=True )
    description = models.TextField(null=True , max_length=200)
    image = models.ImageField(upload_to='skills' , null=True)
    
class Education(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    title = models.CharField(null=True , max_length=50)
    description = models.TextField(null=True , max_length=200)
    academy_title = models.CharField(null=True , max_length=50)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)