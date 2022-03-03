from django.urls import path

from blog.views import BlogListView, CategoryListView, TagListView, BlogDetailView

app_name = 'blog'


urlpatterns = [
    path('article', BlogListView.as_view(), name='article'),
    path('category', CategoryListView.as_view(), name='category'),
    path('tag/all', TagListView.as_view(), name='tag'),
    path('article/hottest', BlogListView.as_view(), name='aHot'),

]
