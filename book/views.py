from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import models
from rest_framework import status
from . import serlaizers
from rest_framework.authtoken.models import Token
from django.contrib.auth import logout
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.http import HttpResponse

# Create your views here.
@api_view(['POST'])
def register(request):
  ser=serlaizers.userser(data=request.data)
  if ser.is_valid():
    ser.save()
    user=models.User.objects.get(username=request.data['username'])
    user.set_password(request.data['password'])
    user.save()
    token=Token.objects.create(user=user)
    return Response({'token':token.key,'user':ser.data})
  else:
    return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)
@api_view(['POST'])
def login(request):
 try:
    user=models.User.objects.get(username=request.data['username'])
    ser=serlaizers.userser(user)
    if user.check_password(request.data['password']):
      token=Token.objects.create(user=user)
      return Response({'token':token.key,'user':ser.data})
    else:
     return Response({'uncorect pass'},status=status.HTTP_400_BAD_REQUEST)
 except models.User.DoesNotExist:
   return Response({'user dont find'},status=status.HTTP_404_NOT_FOUND)
@api_view(['POST'])
def logout_view(request):
    if request.user and request.user.is_authenticated:
      request.user.auth_token.delete()
      return Response({'item delited'})
    else:
      return Response({'you are unathu'})
@api_view(['DELETE'])
def deleteacount(request,token):
  try:
    t=Token.objects.get(key=token)
    t.user.delete()
    return Response({'remmoved'})
  except Token.DoesNotExist:
    return Response(status=400)  


class addbook(APIView):
  permission_classes=[IsAuthenticated]
  def post(self,request):
    ser=serlaizers.bookserlaizer(data=request.data)
    if ser.is_valid():
     ser.save()
     book=models.book.objects.get(title=request.data['title'],pk=ser.data['id'])
     book.author=request.user
     book.save()
     s=serlaizers.bookserlaizer(book)
     return Response(s.data)
    else:
     return Response(ser.errors,status=404)
    
class buybook(APIView):
  permission_classes=[IsAuthenticated]
  def post(self,request):
    hedar=request.headers.get('book')
    bok=models.book.objects.get(pk=hedar)
    bok.buyer.add(request.user)
    bok.save()
    se=serlaizers.bookserlaizer(bok)
    return Response(se.data)

class profilepic(APIView):
  permission_classes=[IsAuthenticated]
  def post(self,request):
    se=serlaizers.profileser(data=request.data)
    if se.is_valid():
      se.save()
      prof=models.profile.objects.get(pk=se.data['id'])
      prof.user=request.user
      prof.save()
      return HttpResponse (prof.user)
    else:
      return Response (se.errors)



