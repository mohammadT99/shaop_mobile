from django.db import models

# Create your models here.
#<<<<<<---------------------category--------------------------->>>
class Category(models.Model):
    titel=models.CharField(max_length=20)
    slug=models.SlugField(max_length=20)
    status=models.BooleanField(default=True)
    position=models.IntegerField()
    class Meta:
        ordering=['position']
    def __str__(self):
        return self.titel
#<<<<<----------------------------------post------------------>>>
class Post(models.Model):
    STATUS_CHOICES={
        ('p','publish'),
        ('d','drsft'),
        
    }
    titel=models.CharField(max_length=20)
    slug=models.SlugField()
    image=models.ImageField( upload_to='image')
    desc=models.TextField()
    publish=models.CharField( max_length=50)
    drct=models.CharField( max_length=50,choices=STATUS_CHOICES)
    def __str__(self):
        return self.titel
#<<<<--------------------------------contact------------------------>>>>

class Contact(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField(max_length=256)
    phone=models.CharField(max_length=12)
    masege=models.TextField()
    def __str__(self):
        return self.email


    