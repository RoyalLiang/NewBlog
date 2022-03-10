# Generated by Django 3.2 on 2022-03-10 06:04

from django.db import migrations, models
import django.db.models.deletion
import mdeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogmodel',
            options={'verbose_name': '博文管理', 'verbose_name_plural': '博文管理'},
        ),
        migrations.AlterField(
            model_name='blogmodel',
            name='author',
            field=models.CharField(db_index=True, max_length=30, verbose_name='作者'),
        ),
        migrations.AlterField(
            model_name='blogmodel',
            name='categories',
            field=models.ManyToManyField(blank=True, related_name='cat_blog', through='blog.BlogRefCategoryModel', to='blog.LabelModel', verbose_name='类别'),
        ),
        migrations.AlterField(
            model_name='blogmodel',
            name='comment',
            field=models.IntegerField(default=0, verbose_name='评论数'),
        ),
        migrations.AlterField(
            model_name='blogmodel',
            name='content',
            field=mdeditor.fields.MDTextField(verbose_name='内容'),
        ),
        migrations.AlterField(
            model_name='blogmodel',
            name='cover',
            field=models.ImageField(blank=True, max_length=200, null=True, upload_to='blog', verbose_name='封面'),
        ),
        migrations.AlterField(
            model_name='blogmodel',
            name='like',
            field=models.IntegerField(default=0, verbose_name='点赞数'),
        ),
        migrations.AlterField(
            model_name='blogmodel',
            name='read',
            field=models.IntegerField(default=0, verbose_name='阅读数'),
        ),
        migrations.AlterField(
            model_name='blogmodel',
            name='status',
            field=models.SmallIntegerField(choices=[(-1, '删除'), (0, '草稿'), (1, '已发布')], default=0, verbose_name='状态'),
        ),
        migrations.AlterField(
            model_name='blogmodel',
            name='summary',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='摘要'),
        ),
        migrations.AlterField(
            model_name='blogmodel',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='tag_blog', through='blog.BlogRefTagModel', to='blog.LabelModel', verbose_name='标签'),
        ),
        migrations.AlterField(
            model_name='blogmodel',
            name='title',
            field=models.CharField(db_index=True, max_length=50, unique=True, verbose_name='标题'),
        ),
        migrations.AlterField(
            model_name='blogrefcategorymodel',
            name='category',
            field=models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, to='blog.labelmodel', verbose_name='类别'),
        ),
        migrations.AlterField(
            model_name='blogreftagmodel',
            name='tag',
            field=models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, to='blog.labelmodel', verbose_name='标签'),
        ),
        migrations.AlterField(
            model_name='labelmodel',
            name='cat',
            field=models.SmallIntegerField(choices=[(1, '标签'), (2, '类别')], db_index=True, verbose_name='类别'),
        ),
        migrations.AlterField(
            model_name='labelmodel',
            name='cover',
            field=models.ImageField(blank=True, max_length=200, null=True, upload_to='label', verbose_name='封面'),
        ),
        migrations.AlterField(
            model_name='labelmodel',
            name='desc',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='描述'),
        ),
        migrations.AlterField(
            model_name='labelmodel',
            name='name',
            field=models.CharField(db_index=True, max_length=30, verbose_name='名称'),
        ),
        migrations.AlterField(
            model_name='labelmodel',
            name='status',
            field=models.SmallIntegerField(choices=[(-1, '已删除'), (0, '草稿'), (1, '使用中')], db_index=True, default=0, verbose_name='状态'),
        ),
    ]