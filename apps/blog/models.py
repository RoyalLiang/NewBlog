from django.db import models

# Create your models here.
from mdeditor.fields import MDTextField

from extra.base.enums import LabelEnum
from extra.base.models import BaseModel


class LabelModel(BaseModel):

    CAT = [
        (1, '标签'),
        (2, '类别')
    ]

    STATUS = [
        (-1, '已删除'),
        (0, '草稿'),
        (1, '使用中')
    ]

    name = models.CharField(max_length=30, db_index=True, verbose_name='名称')
    cover = models.ImageField(max_length=200, upload_to='label', null=True, blank=True, verbose_name='封面')
    desc = models.CharField(max_length=300, null=True, blank=True, verbose_name='描述')
    slogan = models.CharField(max_length=30, verbose_name='标语')
    cat = models.SmallIntegerField(choices=CAT, db_index=True, verbose_name='类别')
    status = models.SmallIntegerField(choices=STATUS, db_index=True, default=0, verbose_name='状态')

    class Meta:
        db_table = 'label'
        verbose_name = '分类管理'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def dict(self, cat='tag'):
        return dict(
            id=self.id, name=self.name, thumb=self.cover.url if self.cover else '', description=self.desc, create_at=str(self.create_time),
            extends=[{'name': "icon", 'value': "icon-taichi"}], articles_count=getattr(self, f'{cat}_blog').count(), slug='ddd'
        )

    @classmethod
    def list(cls, page, page_size, cat, query=None, **kwargs):
        if query:
            query.update({'cat': LabelEnum[cat]})
        else:
            query = {'cat': LabelEnum[cat]}
        labels = cls.get_list(query)
        r = [l.dict() for l in labels]
        return r


class BlogModel(BaseModel):

    STATUS = [
        (-1, '删除'),
        (0, '草稿'),
        (1, '已发布')
    ]

    BASE_URL = 'https://royalliang.oss-cn-shanghai.aliyuncs.com'

    title = models.CharField(max_length=50, db_index=True, unique=True, verbose_name='标题')
    cover = models.ImageField(upload_to='blog', max_length=200, blank=True, null=True, verbose_name='封面')
    author = models.CharField(max_length=30, db_index=True, verbose_name='作者')
    summary = models.CharField(max_length=500, null=True, blank=True, verbose_name='摘要')
    tags = models.ManyToManyField(
        LabelModel, related_name='tag_blog', through='BlogRefTagModel',
        through_fields=('blog', 'tag'), verbose_name='标签', blank=True
    )
    categories = models.ManyToManyField(
        LabelModel, related_name='cat_blog', through='BlogRefCategoryModel',
        through_fields=('blog', 'category'), verbose_name='类别', blank=True
    )
    content = MDTextField(verbose_name='内容')
    status = models.SmallIntegerField(default=0, choices=STATUS, verbose_name='状态')
    read = models.IntegerField(default=0, verbose_name='阅读数')
    comment = models.IntegerField(default=0, verbose_name='评论数')
    like = models.IntegerField(default=0, verbose_name='点赞数')

    class Meta:
        db_table = 'blog'
        verbose_name = '博文管理'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

    def dict(self, detail=False):
        r = dict(
            id=self.id, slug='peace-and-love', title=self.title, thumb=self.cover.url if self.cover else '',
            description=self.summary, author=self.author,
            tag=self._get_label(cat=1), category=self._get_label(cat=2), create_at=str(self.create_time),
            keywords=['ddd'], state=self.status, public=self.status, origin=0, lang='zh', update_at=str(self.update_time),
            extends=[], meta=dict(likes=self.like, views=self.read, comments=self.comment)
        )
        if detail:
            r['content'] = self.content
            self.read += 1
            self.save(update_fields=['read'])
        return r

    @classmethod
    def list(cls, query, page=1, page_size=20, detail=False, **kwargs):
        articles = cls.paginate(cls.get_list(query=query), page, page_size)
        r = [a.dict(detail) for a in articles]
        return r

    def _get_label(self, cat):
        if cat == 1:
            return [t.dict() for t in self.tags.all()]
        elif cat == 2:
            return [c.dict() for c in self.categories.all()]
        else:
            return []


class BlogRefTagModel(BaseModel):
    blog = models.ForeignKey(BlogModel, on_delete=models.CASCADE, db_constraint=False)
    tag = models.ForeignKey(LabelModel, on_delete=models.CASCADE, db_constraint=False, verbose_name='标签')

    class Meta:
        db_table = 'blog_ref_tag'
        verbose_name = 'Tag'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.tag.name


class BlogRefCategoryModel(BaseModel):
    blog = models.ForeignKey(BlogModel, on_delete=models.CASCADE, db_constraint=False)
    category = models.ForeignKey(LabelModel, on_delete=models.CASCADE, db_constraint=False, verbose_name='类别')

    class Meta:
        db_table = 'blog_ref_category'
        verbose_name = 'Category'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.category.name

