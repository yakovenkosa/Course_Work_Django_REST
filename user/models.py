from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(
        unique=True, verbose_name="Почта", help_text="Укажите почту пользователя"
    )
    phone = models.CharField(
        max_length=35,
        verbose_name="Телефон",
        blank=True,
        null=True,
        help_text="Укажите номер телефона пользователя",
    )
    tg_nickname = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        help_text="Укажите никнейм телеграмма",
        verbose_name="Имя в ТГ",
    )
    avatar = models.ImageField(
        upload_to="users/avatars",
        blank=True,
        null=True,
        help_text="Загрузите аватар",
        verbose_name="Аватар",
    )
    tg_chat_id = models.CharField(
        max_length=35,
        blank=True,
        null=True,
        verbose_name="telegram chat id",
        help_text="Укажите chat id в телеграмм",
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
