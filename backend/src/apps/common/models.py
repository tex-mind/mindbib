from django.db import models

from common.db.models import Model

__all__ = ["Image"]


class Image(Model):
    id = models.BigAutoField(primary_key=True)
    hash = models.UUIDField(unique=True, null=True)
    path = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    class Meta:
        db_table = "image"
        verbose_name = "apps:common:image:verbose"
        verbose_name_plural = "apps:common:image:verbose-plural"

    def __str__(self):
        return self.path
