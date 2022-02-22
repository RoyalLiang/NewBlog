from django.db import models


class BaseModel(models.Model):

    create_time = models.DateTimeField(auto_now_add=True, null=False)
    update_time = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        abstract = True
