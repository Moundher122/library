from django.urls import path
from . import views

urlpatterns = [
    path('',views.addbook.as_view()),
    path('register',views.register),
    path('<str:token>/',views.deleteacount),
    path('logout',views.logout_view),
    path('sigin',views.login),
    path('buy',views.buybook.as_view()),
    path('pic',views.profilepic.as_view())
]
