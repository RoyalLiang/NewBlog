from django.db import models

# Create your models here.
from extra.base.model import BaseModel


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
    cover = models.CharField(max_length=200, default='', null=True, blank=True, verbose_name='封面')
    desc = models.CharField(max_length=300, null=True, blank=True, verbose_name='描述')
    cat = models.SmallIntegerField(choices=CAT, db_index=True, verbose_name='类别')
    status = models.SmallIntegerField(choices=STATUS, db_index=True, default=0, verbose_name='状态')

    class Meta:
        db_table = 'label'
        verbose_name = '分类管理'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class BlogModel(BaseModel):

    STATUS = [
        (-1, '删除'),
        (0, '草稿'),
        (1, '已发布')
    ]

    title = models.CharField(max_length=50, db_index=True, unique=True, verbose_name='标题')
    cover = models.CharField(max_length=200, default='', blank=True, null=True, verbose_name='封面')
    author = models.CharField(max_length=30, db_index=True, verbose_name='作者')
    summary = models.CharField(max_length=500, null=True, blank=True, verbose_name='摘要')
    tags = models.ManyToManyField(
        LabelModel, related_name='tag_blog', through='BlogRefTagModel',
        through_fields=('blog', 'tag'), verbose_name='标签'
    )
    categories = models.ManyToManyField(
        LabelModel, related_name='cat_blog', through='BlogRefCategoryModel',
        through_fields=('blog', 'category'), verbose_name='类别'
    )
    content = models.TextField(null=False, verbose_name='内容')
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

