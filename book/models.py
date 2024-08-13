from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class book(models.Model):
  title=models.CharField(max_length=50)
  stock=models.IntegerField()
  cover=models.ImageField( upload_to='images', blank=True)
  buyer=models.ManyToManyField(User,related_name='buyer',null=True)
  author=models.ForeignKey(User, on_delete=models.CASCADE,related_name='author',null=True)


  def __str__(self) :
    return self.title
  

class profile(models.Model):
  profilepic=models.ImageField( upload_to='pics', blank=True,null=True)
  number=models.IntegerField()
  user=models.OneToOneField(
    User,  on_delete=models.CASCADE,null=True)

