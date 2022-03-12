from django.db import models

from mdeditor.fields import MDTextField

# Create your models here.
from blog.models import BlogModel
from extra.base.models import BaseModel


class ArticleCommentModel(BaseModel):

    blog = models.ForeignKey(BlogModel, on_delete=models.CASCADE, db_constraint=False, verbose_name='博客ID')
    nickname = models.CharField(max_length=50, verbose_name='昵称')
    email = models.EmailField(null=True, default='', verbose_name='邮箱')
    pid = models.IntegerField(default=0, verbose_name='parent comment id')
    content = MDTextField(verbose_name='评论内容')

    class Meta:
        db_table = 'blog_comments'
        verbose_name = '评论管理'
        verbose_name_plural = verbose_name

    @classmethod
    def create_comment(cls, data):
        comment = cls.objects.create(
            blog=BlogModel.objects.get(pk=data['post_id']), content=data['content'],
            nickname=data['author']['name'], email=data['author']['email'], pid=data['pid']
        )
        return comment

