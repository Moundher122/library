from rest_framework  import serializers
from django.contrib.auth.models import User
from . import models

class bookserlaizer(serializers.ModelSerializer):
  class Meta:
    model=models.book
    fields='__all__'


  extra_kwargs={
      'buyer': {'required': False,}
   }

class userser(serializers.ModelSerializer):
   class Meta:
    model=User
    fields=['username','first_name','password']


class profileser(serializers.ModelSerializer):
  class Meta:
    model= models.profile
    fields= '__all__'

