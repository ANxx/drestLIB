from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import  views


urlpatterns = [ 


    path('register/',views.RegisterAPIView.as_view()),
    path('register/<int:pk>/',views.RegisterAPIViewDetail.as_view()),
    path('book/',views.BookAPIView.as_view()),
    path('book/<int:pk>/',views.BookAPIViewDetail.as_view()),

]

 

 
   