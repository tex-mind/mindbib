from django.db import models


class Language(models.Model):
    id = models.SmallAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True, help_text="any ISO 3166-1")
    is_active = models.BooleanField(default=True, null=False)

    class Meta:
        db_table = "i18n_language"
        verbose_name = "apps:i18n:language:verbose"
        verbose_name_plural = "apps:i18n:verbose-plural"

    def __str__(self):
        return self.name
