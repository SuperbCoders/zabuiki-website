from django.db import models
from django.utils import timezone


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
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Мобильный текстовый блок на главной {self.pk}"


class SiteConfig(SeoMeta):
    class Meta:
        verbose_name = "Конфигурация"
        verbose_name_plural = "Конфигурация сайта"

    email = models.EmailField("Email организации", blank=True)
    anonce_text = models.CharField("Текст анонса", max_length=100, blank=False)
    anonce_link = models.URLField("Ссылка", blank=False)
    up_text = models.TextField("Левый нижний текст главной страницы",
        max_length=100,
        blank=False,
        default="Gilrs Club, <br> где мы идем <br> на встречу приключениям"
    )
    down_text = models.TextField("Левый нижний текст главной страницы",
        max_length=100,
        blank=False,
        default="Мы – сообщество девушек, <br> классно проводим время, <br> общаемся и дружим."
    )
    image_1_pc = models.ImageField("Изображение 1 главной страницы PC", upload_to="images/home")
    image_2_pc = models.ImageField("Изображение 2 главной страницы PC", upload_to="images/home")
    image_3_pc = models.ImageField("Изображение 3 главной страницы PC", upload_to="images/home")
    image_1_mobile = models.ImageField("Изображение 1 главной страницы Mobile", upload_to="images/home")

    html_head = models.TextField(blank=True)
    html_footer = models.TextField(blank=True)
    enabled = models.BooleanField("Активная конфигурация", default=True)

    def __str__(self):
        return f"Конфигурация сайта zabuiki {self.pk}"


class Social(models.Model):
    class Meta:
        verbose_name = "Соц сеть"
        verbose_name_plural = "Социальные сети"

    name = models.CharField("Название", max_length=50)
    link = models.URLField("Ссылка")
    config = models.ForeignKey(
        SiteConfig, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"Социальная сеть {self.name}"
