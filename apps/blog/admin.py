from django.contrib import admin

# Register your models here.
from blog.models import BlogModel, LabelModel
from extra.base.enums import LabelEnum


class TagInline(admin.TabularInline):
    model = BlogModel.tags.through

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(tag__cat=LabelEnum.TAG)


class CatInline(admin.TabularInline):
    model = BlogModel.categories.through

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(category__cat=LabelEnum.CATEGORY)


@admin.register(LabelModel)
class LabelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'cat', 'create_time', 'status']


@admin.register(BlogModel)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'create_time', 'read', 'like', 'status']
    readonly_fields = ['comment', 'read', 'like']
    exclude = ['tags', 'categories']
    inlines = [TagInline, CatInline]

    # def tags(self, obj):
    #     return [tag.name for tag in LabelModel.objects.filter(cat=LabelEnum.TAG)]
    #
    # def categories(self, obj):
    #     return [cat.name for cat in LabelModel.objects.filter(cat=LabelEnum.CATEGORY)]

