import datetime

from django.contrib.auth.models import (AbstractBaseUser, AbstractUser,
                                        BaseUserManager, Permission,
                                        PermissionsMixin)
from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumber, PhoneNumberField

from .validators import validate_possible_number


class PossiblePhoneNumberField(PhoneNumberField):
    default_validators = [validate_possible_number]


class UserManager(BaseUserManager):
    def create_user(
        self, password=None, is_staff=False, is_active=True, **extra_fields
    ):
        extra_fields.pop("username", None)

        user = self.model(
            is_active=is_active, is_staff=is_staff, **extra_fields
        )

        if password:
            user.set_password(password)
        user.save()

        return user

    def create_superuser(self, password=None, **extra_fields):
        return self.create_user(
            password, is_staff=True, is_superuser=True, **extra_fields
        )

    def staff(self):
        return self.get_queryset().filter(is_staff=True)


class User(AbstractBaseUser, PermissionsMixin):
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    class UserStatus:
        ACTIVE = "0"
        BLOCKED = "1"

        choices = (
            (ACTIVE, "Активен"),
            (BLOCKED, "Заблокирован"),
        )

    class PaymentStatus:
        PAID = "0"
        NOT_PAID = "1"

        choices = (
            (PAID, "Оплачено"),
            (NOT_PAID, "Не оплачено"),
        )

    username = None
    name = models.CharField("Имя пользователя", max_length=100, blank=True)

    email = models.EmailField("Email", blank=True, db_index=True, unique=True)
    phone = PossiblePhoneNumberField(
        "Номер телефона", blank=True, null=True, db_index=True, unique=True)
    status = models.CharField(
        "Статус", max_length=1, choices=UserStatus.choices, default=UserStatus.ACTIVE)
    payment_status = models.CharField(
        "Оплата", max_length=1, choices=PaymentStatus.choices, default=PaymentStatus.NOT_PAID)
    social = models.URLField("Cоцсеть", blank=True)
    telegram = models.CharField("Телеграм", blank=True, max_length=100)
    comment = models.TextField("Комментарий", blank=True)
    birthday = models.DateField("Дата рождения", blank=True)

    is_staff = models.BooleanField("Статус персонала", default=False)
    is_active = models.BooleanField("Активный", default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return f"Пользователь {self.name}"
