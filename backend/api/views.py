from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, ListAPIView
from .models import BlogPost, Category
from .serializers import BlogPostSerializer


# Create your views here.

class BlogPostListView(ListAPIView):
    queryset = BlogPost.objects.order_by('-created_at')
    serializer_class = BlogPostSerializer
    lookup_field = 'slug'
    permission_classes = [permissions.AllowAny]


class BlogPostDetailView(RetrieveAPIView):
    queryset = BlogPost.objects.order_by('-created_at')
    serializer_class = BlogPostSerializer
    lookup_field = 'slug'
    permission_classes = [permissions.AllowAny]


class BlogPostFeaturedListView(ListAPIView):
    queryset = BlogPost.objects.filter(featured=True).order_by('-created_at')
    serializer_class = BlogPostSerializer
    lookup_field = 'slug'
    permission_classes = [permissions.AllowAny]


class BlogPostCategoryListView(APIView):
    serializer_class = BlogPostSerializer
    permissions_classes = [permissions.AllowAny]

    def post(self, request, format=None):
        data = self.request.data
        category = data['category']
        queryset = BlogPost.objects.filter(category=category).order_by('-created_at')
        serializer = BlogPostSerializer(queryset, many=True)
        return Response(serializer.data)


