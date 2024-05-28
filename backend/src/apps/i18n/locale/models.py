from django.db import models


class TranslationKey(models.Model):
    key = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True)

    class Meta:
        db_table = "i18n_locale_translation_key"
        verbose_name = "apps:i18n:locale:translation-key:verbose"
        verbose_name_plural = "apps:i18n:locale:translation-key:verbose-plural"

    def __str__(self):
        return self.key


class Translation(models.Model):
    key = models.ForeignKey("locale.TranslationKey", on_delete=models.CASCADE, related_name="translations")
    language = models.ForeignKey("i18n.Language", on_delete=models.CASCADE)
    text = models.TextField(null=False)

    class Meta:
        unique_together = ("key", "language")
        db_table = "i18n_locale_translation"
        verbose_name = "apps:i18n:locale:translation:verbose"
        verbose_name_plural = "apps:i18n:locale:translation:verbose-plural"

    def __str__(self):
        return f"{self.key.key} ({self.language.code})"
