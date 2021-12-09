from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny,IsAuthenticated

from .models import Library
from .serializers import RegisterSerializer,BookSerializer
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication



class RegisterAPIView(generics.ListCreateAPIView):
    '''
     listing a queryset or creating a model instance.
    '''
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    

class RegisterAPIViewDetail(generics.RetrieveUpdateDestroyAPIView):
    '''
    view for retrieving, updating or deleting a model instance.
    '''
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class BookAPIView(generics.ListCreateAPIView):
    queryset = Library.objects.all()
    serializer_class = BookSerializer
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (AllowAny,)

class BookAPIViewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Library.objects.all()
    serializer_class = BookSerializer
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated, )
    
