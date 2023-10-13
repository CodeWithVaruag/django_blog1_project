from django.db import models
from django.utils.html import format_html


# Create your models here.

#categories table
class Category(models.Model):
    Category_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=100)
    description=models.TextField()
    urls=models.CharField(max_length=100)
    image=models.ImageField(upload_to='Category/')
    date=models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.title
    

class Post(models.Model):
    Post_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=200)
    content=models.TextField()
    urls=models.CharField(max_length=100)
    Category=models.ForeignKey(Category,on_delete=models.CASCADE) 
    image=models.ImageField(upload_to='Post/')
    date=models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.title
    




