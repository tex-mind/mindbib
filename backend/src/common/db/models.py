from typing import TypeVar

from django.db import models

from .exceptions import DuplicateRecordError, RecordNotFoundError

DjangoModel = TypeVar("DjangoModel", bound=models.Model)


class QuerySet(models.QuerySet):
    def get(self, *args, **kwargs) -> DjangoModel | None:
        try:
            return self.get(*args, **kwargs)
        except self.model.DoesNotExist:
            raise RecordNotFoundError
        except self.model.MultipleObjectsReturned:
            raise DuplicateRecordError


class Model(models.Model):
    objects = QuerySet.as_manager()

    class Meta:
        abstract = True
