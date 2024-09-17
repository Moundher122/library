from rest_framework  import serializers
from django.contrib.auth.models import User
from . import models

class bookserlaizer(serializers.ModelSerializer):
  class Meta:
    model=models.book
    fields=['title','cover','stock','price','id']


  extra_kwargs={
      'buyer': {'required': False,}
   }

class userser(serializers.ModelSerializer):
   class Meta:
    model=User
    fields=['username','email','password']

class buyerser(serializers.ModelSerializer):
  class Meta:
    model=models.buyer
    fields='__all__'


class profileser(serializers.ModelSerializer):
  class Meta:
    model= models.profile
    fields= '__all__'


class bookauthserlaizer(serializers.ModelSerializer):
  class Meta:
    model=models.book
    fields='__all__'
