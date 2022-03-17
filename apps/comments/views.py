from django.shortcuts import render

from loguru import logger
# Create your views here.
from comments.models import ArticleCommentModel
from extra.base.views import BasePostView, BaseGetView
from extra.decorate import catch_page
from extra.base.views import BasePostView


class PostCommentView(BasePostView):

    def _process(self, request, *args, **kwargs):
        logger.info(f"post comment req: {self.req}")
        comment = ArticleCommentModel.create_comment(self.req)
        r = comment.dict()
        return self.response(data=r)


class CommentView(BaseGetView):

    @catch_page
    def _process(self, request, *args, **kwargs):
        comments = ArticleCommentModel.list({}, self.page, self.page_size)
        p = {'total': 1, 'current_page': 1, 'per_page': 1, 'total_page': 1}
        return self.response(data={'data': comments, 'pagination': p})


class VoteCommentView(BasePostView):

    def _process(self, request, *args, **kwargs):
        try:
            comment, r = ArticleCommentModel.vote_comment(self.req['comment_id'], self.req['vote'])
        except AttributeError:
            logger.error(f"comment id {self.req['comment_id']} not found")
        else:
            data = dict(likes=comment.likes, dislikes=comment.dislikes)
            if r:
                return self.response(data=data)
            else:
                return self.response(data=data, code='waring', msg='get unsupport operation')

