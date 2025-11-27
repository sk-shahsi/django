from rest_framework.response import Response
from rest_framework.decorators import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from helloworld.serializers import postSerializer
from helloworld.models import Post
from helloworld.permissions import IsPostPossessor
from helloworld.filters import PostFilter


class HelloWorld(APIView):
    def get(self, request):
        return Response({'message': 'Hello, World!'})


class postView(ModelViewSet):
    permission_classes = [IsAuthenticated, IsPostPossessor]
    serializer_class = postSerializer

    filter_backends = [DjangoFilterBackend, filters.SearchFilter,filters.OrderingFilter]
    filter_class = PostFilter
    queryset = Post.objects.all()
    filterset_class = PostFilter
    ordering_fields = ['id']
    search_fields = ['title', 'content']

    def get_queryset(self):
        return Post.objects.filter(created_by=self.request.user)
