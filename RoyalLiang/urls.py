"""RoyalLiang URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from blog.views import CommonView, CategoryListView, TagListView, BlogListView, CalendarView, HotBlogListView, \
    ConfigView, OptionView, BlogDetailView, BlogContextView
from comments.views import PostCommentView, CommentView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('blog.urls', namespace='blog')),
    path('option', OptionView.as_view()),
    path('disqus/config', ConfigView.as_view()),
    path('category', CategoryListView.as_view(), name='category'),
    path('tag/all', TagListView.as_view(), name='tag'),
    path('article/hottest', HotBlogListView.as_view(), name='aHot'),
    path('article', BlogListView.as_view(), name='article'),
    path('article/<int:pid>', BlogDetailView.as_view(), name='articleDetail'),
    path('article/<int:pid>/context', BlogContextView.as_view(), name='articleDetailContext'),
    path('article/calendar', CalendarView.as_view(), name='calendar'),
    path('comment', CommentView.as_view(), name='comment'),
    path('disqus/comment', PostCommentView.as_view(), name='postComment'),
    # path('vote/comment', '', name='voteComment'),

]
