from django.contrib.auth.models import User
from rest_framework import serializers
from .models import BlogPost, Category


class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = '__all__'
        lookup_field = 'slug'
