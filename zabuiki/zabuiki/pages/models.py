from autoslug import AutoSlugField
from django.db import models
from django.utils import timezone

from zabuiki.pages.default_content_html import HTML
from zabuiki.site_conf.models import Lecturers, SeoMeta


class Category(models.Model):
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории страниц"
        ordering = ["-created"]

    name = models.CharField('Название', max_length=155)
    is_view = models.BooleanField("Отображать на сайте", default=True)
    slug = AutoSlugField("Url", populate_from='title', editable=True,
                         help_text="Привет мир -> privet-mir, privet_mir, hellow-world")
    created = models.DateTimeField("Дата создания", default=timezone.now)
    
    def __str__(self):
        return self.name


class Page(SeoMeta):
    class Meta:
        verbose_name = "Страница"
        verbose_name_plural = "Текстовые страницы"
        ordering = ["created"]

    title = models.CharField('Заголовок', max_length=155)
    category = models.ForeignKey(Category, verbose_name="Категория", null=True, on_delete=models.SET_NULL)

    html_text = models.TextField("Html", default=HTML)
    is_view = models.BooleanField("Отображать на сайте", default=True)
    image = models.ImageField("Заглавное изображение",
                              upload_to="images/pages/main")
    created = models.DateTimeField("Дата создания", default=timezone.now)
    lecturer = models.ForeignKey(Lecturers, verbose_name="Лектор", null=True, on_delete=models.SET_NULL)
    link = models.URLField("Ссылка кнопки записаться", default="/")

    def __str__(self):
        return self.title


class PageMobileSlider(models.Model):
    class Meta:
        verbose_name = "Слайд"
        verbose_name_plural = "Мобильный Слайдер"

    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    image = models.ImageField("Изображение", upload_to="images/pages/slider")

    def __str__(self):
        return ""
