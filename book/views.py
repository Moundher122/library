from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import models
from rest_framework import status
from . import serlaizers
from rest_framework.authtoken.models import Token
from django.contrib.auth import logout
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
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
    return Response({'token':token.key,'user':ser.data,'created':user.date_joined})
  else:
    return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)
@api_view(['POST'])
def login(request):
 try:
    user=models.User.objects.get(username=request.data['username'])
    ser=serlaizers.userser(user)
    if user.check_password(request.data['password']):
      token,create=Token.objects.get_or_create(user=user)
      return Response({'token':token.key,'user':ser.data,'created':user.date_joined})
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
def deleteacount(request):
  token=request.headers.get('Authorization')
  try:
    t=Token.objects.get(key=token)
    t.user.delete()
    return Response({'remmoved'})
  except Token.DoesNotExist:
    return Response(status=400)  
  
class addbook(APIView):
  permission_classes=[IsAuthenticated]
  def post(self,request):
    print(request.data)
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
    
class getbooks(APIView):
  permission_classes=[IsAuthenticated]
  def get(self,request):
    books=models.book.objects.all()
    m=[]
    for book in books :
      se=serlaizers.bookserlaizer(book)
      m.append({'book':se.data,'author':serlaizers.userser(book.author).data['username'],'buyer':book.buyers.count()})
    return Response({'books':m})


class getbooksuadd(APIView):
  permission_classes=[IsAuthenticated]
  def get(self,request):
    try:
      bk=models.book.objects.filter(author=request.user)
      m=[]
      for book in bk :
       se=serlaizers.bookserlaizer(book)
       m.append({'book':se.data,'author':serlaizers.userser(book.author).data['username'],'buyer':book.buyers.count()})
      return Response({'books':m})
    except models.book.DoesNotExist:
      return Response(status=401)
    

class buybook(APIView):
  permission_classes=[IsAuthenticated]
  def post(self,request):
    hedar=request.headers.get('book')
    bok=models.book.objects.get(pk=hedar)
    if bok.stock>=1:
      ser=serlaizers.buyerser(data=request.data)
      if ser.is_valid():
        ser.save()
        buyer=models.buyer.objects.get(pk=ser.data['id'])
        buyer.user=request.user
        buyer.save()
        bok.buyers.add(buyer)
        bok.stock=bok.stock-1
        bok.save()
        se=serlaizers.bookserlaizer(bok)
        return Response(se.data)
      else:
        return Response(status=400)
    else:
      return Response({'this item is out of the stock'})
    
class profilepic(APIView):
  permission_classes=[IsAuthenticated]
  def post(self,request):
    try:
      user=models.profile.objects.get(user=request.user)
      se=serlaizers.profileser(user,request.data)
      if se.is_valid():
       se.save()
       return Response(se.data)
      else:
       return Response (se.errors)
    except models.profile.DoesNotExist:
      se=serlaizers.profileser(data=request.data)
      if se.is_valid():
       se.save(user=request.user)
       return Response(se.data)
      else:
       return Response (se.errors)

    
class profilesup(APIView):
  permission_classes=[IsAuthenticated]
  def delete(self,request):
    try:
       request.user.profile.profilepic.delete() 
       return Response({'profile is deleted'})
    except AttributeError:
      return Response({'user dosent have profile pic'},status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getprofilepic(request):
  try:
    h=models.profile.objects.get(user=request.user)
    se=serlaizers.profileser(h).data['profilepic']
    return Response({'pic':se})
  except models.profile.DoesNotExist:
    return Response(status=401)

@api_view(['DELETE'])
def deleterbook(request):
  hed=request.headers.get('book')
  book=models.book.objects.get(pk=hed)
  if book.author==request.user :
    book.delete()
    return Response({'item deleted'})
  else:
    return Response(status=status.HTTP_401_UNAUTHORIZED)



