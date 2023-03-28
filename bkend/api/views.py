from django.shortcuts import render
from .serializers import UserSerializer
from rest_framework.generics import ListAPIView
from .models import Udata
# Create your views here.
class userlist(ListAPIView):
    queryset = Udata.objects.all()
    serializer_class = UserSerializer