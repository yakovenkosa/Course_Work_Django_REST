from datetime import timedelta

from django.db import models

from config.settings import AUTH_USER_MODEL


class Habit(models.Model):
    user = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Создатель привычки",
        blank=True,
        null=True,
    )
    place = models.CharField(max_length=100, verbose_name="Место выполнения привычки")
    time = models.TimeField(verbose_name="Время выполнения привычки")
    action = models.TextField(verbose_name="Что необходимо выполнить")
    pleasant_habit_sign = models.BooleanField(
        verbose_name="Признак приятной привычки", default=False
    )
    related_habit = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        verbose_name="Связанная привычка",
        blank=True,
        null=True,
    )
    periodicity = models.SmallIntegerField(
        default=1, verbose_name="Периодичность выполнения привычки"
    )
    reward = models.CharField(
        max_length=150,
        verbose_name="Вознаграждение за выполнение",
        blank=True,
        null=True,
    )
    duration = models.DurationField(
        verbose_name="Продолжительность выполнения", default=timedelta(minutes=2)
    )
    is_published = models.BooleanField(
        verbose_name="Признак публичности привычки", default=True
    )
