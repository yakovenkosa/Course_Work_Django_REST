from datetime import timedelta

from rest_framework.exceptions import ValidationError


class DurationValidator:
    """Проверяет длительность выполнения привычки, она не должна превышать 120 секунд."""

    def __init__(self, duration):
        self.duration = duration

    def __call__(self, habit):
        max_duration = timedelta(minutes=2)
        if habit.get(self.duration) and habit.get(self.duration) > max_duration:
            raise ValidationError(
                f"Выполнение не может длиться более {max_duration} секунд."
            )


class PeriodicityValidator:
    """Проверяет, является ли периодичность привычки корректной (не реже чем 1 раз в 7 дней)."""

    def __init__(self, periodicity):
        self.periodicity = periodicity

    def __call__(self, habit):
        if habit.get(self.periodicity) not in range(1, 8):
            raise ValidationError(
                "Периодичность привычки должна быть не реже 1 раза за 7 дней."
            )


class ChoiceRewardValidator:
    """Исключает одновременный выбор вознаграждения и приятной привычки."""

    def __init__(self, related_habit, reward):
        self.related_habit = related_habit
        self.reward = reward

    def __call__(self, habit):
        if habit.get(self.related_habit) and habit.get(self.reward):
            raise ValidationError(
                f"""Нельзя выбрать {self.related_habit} и {self.reward} одновременно, 
            выберите награду или приятную привычку."""
            )


class PleasantHabitValidator:
    """Проверка, является ли привычка приятной."""

    def __init__(self, related_habit, pleasant_habit_sign):
        self.related_habit = related_habit
        self.pleasant_habit_sign = pleasant_habit_sign

    def __call__(self, habit):
        if habit.get(self.related_habit) and not habit.get(self.pleasant_habit_sign):
            raise ValidationError("Привычка не является приятной")


class AbsenceValidator:
    """Проверка на отсутствие награды или связанной приятной привычки за выполнение приятной привычки."""

    def __init__(self, reward, related_habit, pleasant_habit_sigh):
        self.reward = reward
        self.related_habit = related_habit
        self.pleasant_habit_sigh = pleasant_habit_sigh

    def __call__(self, habit):
        if (
            habit.get(self.pleasant_habit_sigh)
            and habit.get(self.reward)
            or habit.get(self.related_habit)
        ):
            raise ValidationError(
                "Приятная привычка не должна иметь вознаграждения или связанную привычку."
            )
