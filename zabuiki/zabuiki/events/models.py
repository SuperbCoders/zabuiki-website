from django.db import models
from django.utils import timezone

from zabuiki.site_conf.models import SeoMeta


class Event(models.Model):
    class Meta:
        verbose_name = "Событие"
        verbose_name_plural = "Расписание событий"
       
       
    name = models.CharField("Название", max_length=68)
    is_free = models.BooleanField(
        "Бесплатное", default=False, help_text="Если указать этот параметр стоимость вводить не нужно")
    price = models.DecimalField('Стоимость',
        default=0,
        max_digits=10,
        decimal_places=2,
        help_text="Укажите стоимость, если параметр 'Бесплатное' не задан" 
    )
    event_time = models.DateTimeField("Дата и время события", default=timezone.now)
    html_code = models.TextField("Html код", blank=True)
    is_view = models.BooleanField("Отображать на сайте", default=True)

    def __str__(self):
        return self.name