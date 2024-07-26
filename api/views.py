from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Blogpost
from .serializer import BlogPostSerializer

class BlogPostListCreate(generics.ListCreateAPIView):
    queryset = Blogpost.objects.all()
    serializer_class = BlogPostSerializer
    def delete(self, request, *args, **kwargs):
        Blogpost.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class BlogRetriveUploadDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blogpost.objects.all()
    serializer_class = BlogPostSerializer
    lookup_feild = "pk"

