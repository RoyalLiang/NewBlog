from django.shortcuts import render

# Create your views here.
from blog.models import BlogModel
from extra.base.views import BaseView, BaseGetView


class BlogListView(BaseGetView):

    def _process(self, request):
        page = int(self.args.get('page', 1))
        page_size = int(self.args.get('pageSize', 20))
        if page or page_size <= 0:
            return self.response()
        articles = BlogModel.list({}, page, page_size)
        return self.response(data=articles)

