from django.shortcuts import render
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import APIView
from helloworld.serializers import postSerializer
from rest_framework.viewsets import ModelViewSet
from helloworld.models import Post


# Create your views here.
class HelloWorld(APIView):
    def get(self,request):
        return Response({'message':'Hello, World!'})

class postView(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = postSerializer
