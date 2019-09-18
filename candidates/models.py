from django.db import models

# Create your models here.

class User(models.Model):
    USER_TYPE_CHOICES = [('ADMIN','Administration'),('F','Faculty')]
    name = models.CharField(max_length=50)
    user_type = models.CharField(choices=USER_TYPE_CHOICES,max_length=5,blank=False)
    
    def __str__(self):
        return self.name
    
class Job(models.Model):
    CATEGORY_CHOICES = [('CS','Computer Science'),('BBA','Business Administration')]
    title = models.CharField(max_length=50)
    category = models.CharField(choices=CATEGORY_CHOICES,max_length=3,blank=False)

    def __str__(self):
        return self.title
        
    
class Candidate(models.Model):
    name = models.CharField(max_length=50)
    skills = models.CharField(max_length=800)
    cv = models.FileField(upload_to='pdfs/', null=True, blank=True)   
    
    def __str__(self):
        return self.name
    
    
    