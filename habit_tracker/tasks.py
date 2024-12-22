from datetime import datetime, timedelta

import pytz
from celery import shared_task

from config import settings
from habit_tracker.models import Habit
from habit_tracker.services import send_telegram_message
from user.models import User


@shared_task
def send_remainder():
    """функция создаёт оповещение в телеграм, о том что нужно сделать для выполнения привычки, количество времени на выполнение и
    награде."""
    habits = Habit.objects.all()
    users = User.objects.all()
    for user in users:
        if user.tg_chat_id:
            for habit in habits:
                habit_start_time = habit.time.replace(second=0, microsecond=0)
                habit_time_now = datetime.now(
                    pytz.timezone(settings.TIME_ZONE)
                ).replace(second=0, microsecond=0)
                if habit_start_time == habit_time_now:
                    if habit.pleasant_habit_sign:
                        send_telegram_message(
                            habit.owner.tg_chat_id,
                            f"Необходимо выполнить: {habit.action}, "
                            f"время выполнения: {habit.duration} минуты.",
                        )
                    if habit.related_habit:
                        send_telegram_message(
                            habit.owner.tg_chat_id,
                            f"Необходимо выполнить: {habit.action}, "
                            f"время выполнения: {habit.duration} минуты, "
                            f"после этого можно будет сделать: {habit.related_habit}.",
                        )
                    if habit.reward:
                        send_telegram_message(
                            habit.owner.tg_chat_id,
                            f"Необходимо выполнить: {habit.action}, "
                            f"время выполнения: {habit.duration} минуты, "
                            f"в награду ты получишь: {habit.reward}.",
                        )
                    habit.time = datetime.now(
                        pytz.timezone(settings.TIME_ZONE)
                    ) + timedelta(days=habit.periodicity)
                    habit.save()
