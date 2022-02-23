from django.contrib import admin

# Register your models here.
from django.contrib.admin import widgets

from blog.models import BlogModel, LabelModel
from extra.base.enums import LabelEnum


class BaseInline(admin.StackedInline):
    extra = 0

    def has_add_permission(self, request, obj):
        return False

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        kwargs["queryset"] = self._get_self_queryset()
        kwargs['widget'] = widgets.FilteredSelectMultiple(db_field.verbose_name, db_field.name in self.filter_vertical)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    @staticmethod
    def _get_self_queryset():
        pass


class TagInline(BaseInline):
    model = BlogModel.tags.through

    @staticmethod
    def _get_self_queryset():
        return LabelModel.objects.filter(cat=LabelEnum.TAG)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(tag__cat=LabelEnum.TAG)


class CatInline(BaseInline):
    model = BlogModel.categories.through

    @staticmethod
    def _get_self_queryset():
        return LabelModel.objects.filter(cat=LabelEnum.CATEGORY)

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
    
    def save_model(self, request, obj, form, change):
        print(form)
        super(BlogAdmin, self).save_model(request, obj, form, change)


