import traceback

from django.core.paginator import Paginator as _Paginator
from django.db import models

from loguru import logger


class BaseModel(models.Model):

    create_time = models.DateTimeField(auto_now_add=True, null=False)
    update_time = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        abstract = True

    @classmethod
    def get_list(cls, query: dict = None, order='desc', *args, **kwargs):
        items = cls.objects.all()
        if query:
            try:
                items = items.filter(**query)
            except Exception:
                logger.error(f"get {cls.__name__} list error, msg: {traceback.format_exc()}")
        if order == 'desc':
            items = items.order_by('-id')
        return items

    @classmethod
    def paginate(cls, queryset, page, page_size):
        items = Paginator(queryset, page_size)
        return items.page(page)


class Paginator(_Paginator):
    pass
