from django.urls import path
from . import views


urlpatterns = [
    path('', views.BlogPostListView.as_view(), name='list'),
    path('feature/', views.BlogPostFeaturedListView.as_view(), name='feature'),
    path('category/', views.BlogPostCategoryListView.as_view(), name='category'),
    path('<slug:slug>/', views.BlogPostDetailView.as_view(), name='detail'),
]
