from django.db import models

from mdeditor.fields import MDTextField

# Create your models here.
from blog.models import BlogModel
from extra.base.models import BaseModel


class ArticleCommentModel(BaseModel):

    blog = models.ForeignKey(BlogModel, on_delete=models.CASCADE, db_constraint=False, verbose_name='博客ID')
    nickname = models.CharField(max_length=50, verbose_name='昵称')
    email = models.EmailField(null=True, default='', verbose_name='邮箱')
    pid = models.IntegerField(default=0, verbose_name='父评论ID')
    content = MDTextField(verbose_name='评论内容')
    likes = models.IntegerField(default=0, verbose_name='赞同数')
    dislikes = models.IntegerField(default=0, verbose_name='反对数')
    status = models.SmallIntegerField(default=1, verbose_name='状态')

    class Meta:
        db_table = 'blog_comments'
        verbose_name = '评论管理'
        verbose_name_plural = verbose_name

    def dict(self, detail=False, **kwargs):
        return dict(
            id=self.id, content=self.content, agent='', author=dict(name=self.nickname, email=self.email, site=''),
            extends=[], state=self.status, likes=self.likes, dislikes=self.dislikes, create_at=str(self.create_time),
            ip_location=dict(country='China', country_code='CN', region='Shanghai', city='Pudong', zip='')
        )

    @classmethod
    def create_comment(cls, data):
        comment = cls.objects.create(
            blog=BlogModel.objects.get(pk=data['post_id']), content=data['content'],
            nickname=data['author']['name'], email=data['author']['email'], pid=data['pid']
        )
        return comment

    @classmethod
    def list(cls, query, page=1, page_size=20, detail=False, **kwargs):
        comments = cls.paginate(cls.get_list(query=query), page, page_size)
        r = [c.dict(detail) for c in comments]
        return r

