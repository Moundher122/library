from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class buyer(models.Model):
  wilaya=models.CharField(max_length=20)
  number=models.IntegerField(max_length=10)
  user=models.ForeignKey(User,  on_delete=models.CASCADE,null=True)


class book(models.Model):
  title=models.CharField(max_length=50)
  stock=models.IntegerField()
  price=models.IntegerField(null=True)
  cover=models.ImageField( upload_to='images', blank=True)
  buyers=models.ManyToManyField(buyer,related_name='buyer',null=True)
  author=models.ForeignKey(User, on_delete=models.CASCADE,related_name='author',null=True)


  def __str__(self) :
    return self.title

class profile(models.Model):
  profilepic=models.ImageField( upload_to='pics', blank=True,null=True)
  user=models.OneToOneField(User,  on_delete=models.CASCADE,null=True)

