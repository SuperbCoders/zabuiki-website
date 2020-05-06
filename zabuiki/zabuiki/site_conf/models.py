from django.db import models
from django.utils import timezone
from zabuiki.site_conf import default_text


class SeoMeta(models.Model):
    meta_title = models.CharField("Meta title", max_length=68, blank=True)
    meta_description = models.TextField(
        "Meta description", max_length=155, blank=True)
    meta_image = models.ImageField("Meta image", upload_to="config/meta", default='default.jpg')

    class Meta:
        abstract = True


class MobileHomeBlocks(models.Model):
    class Meta:
        verbose_name = "Мобильный блок на главной"
        verbose_name_plural = "Мобильные блоки на главной"
        ordering = ["created"]

    image = models.ImageField("Изображение", upload_to="images/home")
    text = models.TextField("Текст")
    is_view = models.BooleanField("Отображать на сайте", default=True)
    created = models.DateTimeField("Дата создания", default=timezone.now)

    def __str__(self):
        return f"Мобильный текстовый блок на главной {self.pk}"


class HomeMobileSlider(models.Model):
    class Meta:
        verbose_name = "Слайд"
        verbose_name_plural = "Мобильный Слайдер на главной"

    image = models.ImageField("Изображение", upload_to="images/home/slider")

    def __str__(self):
        return f"Слайд {self.pk}"


class SiteConfig(SeoMeta):
    class Meta:
        verbose_name = "Конфигурация"
        verbose_name_plural = "Конфигурация сайта"

    email = models.EmailField("Email организации", blank=True)
    anonce_text = models.CharField("Текст анонса", max_length=100, blank=False, default=default_text.HOME_ANONCE)
    anonce_link = models.URLField("Ссылка", blank=False, default="https://google.com")
    up_text = models.TextField("Левый верхний текст главной страницы",
        max_length=100,
        blank=False,
        default=default_text.HOME_TOP_TEXT,
    )
    down_text = models.TextField("Левый нижний текст главной страницы",
        max_length=100,
        blank=False,
        default=default_text.HOME_BOTTOM_TEXT,
    )
    image_1_pc = models.ImageField("Изображение 1 главной страницы PC", upload_to="images/home")
    image_2_pc = models.ImageField("Изображение 2 главной страницы PC", upload_to="images/home")
    image_3_pc = models.ImageField("Изображение 3 главной страницы PC", upload_to="images/home")

    html_head = models.TextField(blank=True)
    html_footer = models.TextField(blank=True)

    about_page_main_text = models.TextField(
        "Заголовок", default=default_text.ABOUT_PAGE_MAIN)

    about_page_top_first_text = models.TextField(
        "Верхний текст 1", default=default_text.ABOUT_PAGE_TOP_ITEM_1)
        
    about_page_top_second_text = models.TextField(
        "Верхний текст 2", default=default_text.ABOUT_PAGE_TOP_ITEM_2)

    about_page_bottom_html = models.TextField(
        "Нижний html", default=default_text.ABOUT_PAGE_BOTTOM)
  

    about_page_direcor = models.CharField(
        "Директор", 
        max_length=100, 
        blank=False, 
        default="МАША ТИМОШЕНКО"
    )
    about_page_direcor_image = models.ImageField("Изображение директора", upload_to="images/about")

    enabled = models.BooleanField("Активная конфигурация", default=True)

    def __str__(self):
        return f"Конфигурация сайта zabuiki {self.pk}"


class Social(models.Model):
    class Meta:
        verbose_name = "Соц сеть"
        verbose_name_plural = "Социальные сети"

    name = models.CharField("Название", max_length=50)
    link = models.URLField("Ссылка")
    

    def __str__(self):
        return f"Социальная сеть {self.name}"


class Lecturers(models.Model):
    class Meta:
        verbose_name = "Участники"
        verbose_name_plural = "Список участников"

    name = models.CharField("ФИО", max_length=155)
    position = models.CharField("Должность", max_length=155)
    image = models.ImageField("Изображение", upload_to="images/about")
    text = models.TextField("Описание", blank=False)

    def __str__(self):
        return f"Лектор {self.name}"