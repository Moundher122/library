from django.urls import path
from . import views

urlpatterns = [
    path('',views.addbook.as_view()),
    path('register',views.register),
    path('del/',views.deleteacount),
    path('logout',views.logout_view),
    path('sigin',views.login),
    path('buy',views.buybook.as_view()),
    path('pic',views.profilepic.as_view()),
    path('sup',views.profilesup.as_view()),
    path('books',views.getbooks.as_view()),
    path('booksu',views.getbooksuadd.as_view()),
    path('image',views.getprofilepic),
    path('delet',views.deleterbook),
]
