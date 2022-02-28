from django.shortcuts import render

# Create your views here.
from blog.models import BlogModel
from extra.base.views import BaseView, BaseGetView


class BlogListView(BaseGetView):

    def _process(self, request):
        articles = BlogModel.list({})
        return self.response(data=articles)

