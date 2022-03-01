from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View

from blog.models import BlogModel, LabelModel
from extra.base.views import BaseView, BaseGetView


class CommonView(View):

    def get(self, request):
        return HttpResponse('SUCCESS')

    def post(self, request):
        return HttpResponse('SUCCESS')


class BlogListView(BaseGetView):

    def _process(self, request):
        if self.page <= 0 or self.page_size <= 0:
            return self.response()
        articles = BlogModel.list({}, self.page, self.page_size)
        return self.response(data=articles)


class CategoryListView(BaseGetView):

    def _process(self, request):
        if self.page <= 0 or self.page_size <= 0:
            return self.response()
        cats = LabelModel.list(self.page, self.page_size, cat='CATEGORY')
        return self.response(data=cats)


class TagListView(BaseGetView):

    def _process(self, request):
        if self.page <= 0 or self.page_size <= 0:
            return self.response()
        tags = LabelModel.list(self.page, self.page_size, cat='TAG')
        return self.response(data=tags)
