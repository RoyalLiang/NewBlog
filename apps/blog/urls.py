from django.urls import path

from blog.views import BlogListView

app_name = 'blog'


urlpatterns = [
    path('aList', BlogListView.as_view(), name='a_list'),
]
