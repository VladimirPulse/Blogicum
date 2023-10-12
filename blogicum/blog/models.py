from django.contrib.auth import get_user_model
from django.db import models
from core.models import PublishedModel


User = get_user_model()

class Category(PublishedModel):
    title = models.CharField(
        max_length=256,
        verbose_name='Название'
        )
    description = models.TextField(verbose_name='Текст')
    slug = models.SlugField(
        max_length=64,
        unique=True,
        verbose_name='Слаг'
        )

    class Meta:
            verbose_name = 'категория'
            verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title             


class Location(PublishedModel):
    name = models.CharField(
        max_length=256,
        verbose_name='Название места'
        )

    class Meta:
            verbose_name = 'Географическая метка'
            verbose_name_plural = 'Географические метки'

    def __str__(self):
        return self.name             



class Post(PublishedModel):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    pub_date = models.DateTimeField(verbose_name='Дата, время')
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE
        )
    location = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
        )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True
        )

    class Meta:
            verbose_name = 'Публикация'
            verbose_name_plural = 'Публикации'

    def __str__(self):
        return self.title             


