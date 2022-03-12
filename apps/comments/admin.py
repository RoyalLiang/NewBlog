from django.contrib import admin

# Register your models here.
from comments.models import ArticleCommentModel


@admin.register(ArticleCommentModel)
class BlogCommentsAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return False
