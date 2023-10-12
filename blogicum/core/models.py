from django.db import models


class PublishedModel(models.Model):
    """Абстрактная модель. Добвляет флаги."""
    is_published = models.BooleanField(
        default=True,
        verbose_name='Опубликовано'
        )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Создано: дата, время'
        )

    class Meta:
        abstract = True