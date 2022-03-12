from django.shortcuts import render

from loguru import logger
# Create your views here.
from comments.models import ArticleCommentModel
from extra.base.views import BasePostView


class PostCommentView(BasePostView):

    def _process(self, request, *args, **kwargs):
        logger.info(f"post comment req: {self.req}")
        ArticleCommentModel.create_comment(self.req)
        return self.response()
