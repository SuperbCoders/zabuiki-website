from django.db import models
from zabuiki.site_conf.models import SeoMeta
from django.utils import timezone
from autoslug import AutoSlugField


class Page(SeoMeta):
    class Meta:
        verbose_name = "Страница"
        verbose_name_plural = "Текстовые страницы"
        ordering = ["created"]

    title = models.CharField('Заголовок', max_length=155,
                             help_text="Ссылка может автоматически формироваться по заголовку")
    slug = AutoSlugField("Ссылка", populate_from='title', editable=True, help_text="Привет мир -> privet-mir, privet_mir, hellow-world")
    nav_name = models.CharField('Название для меню', max_length=50)
    html_text = models.TextField("Html", blank=True)
    is_view = models.BooleanField("Отображать на сайте", default=True)
    created = models.DateTimeField("Дата создания", default=timezone.now)

    def __str__(self):
        return self.title
    