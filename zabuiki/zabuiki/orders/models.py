from django.db import models
from zabuiki.events.models import Event


class Order(models.Model):
    product = models.ForeignKey(Event, verbose_name='Товар', on_delete=models.CASCADE)
    payment = models.ForeignKey('yandex_money.Payment',
                                verbose_name='Платеж',
                                on_delete=models.CASCADE)
    amount = models.PositiveIntegerField('Сумма заказа')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

        