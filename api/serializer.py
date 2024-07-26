from rest_framework import serializers
from .models import Blogpost

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blogpost
        fields = ["id", "title", "content", "published_date"]