from rest_framework import generics, viewsets
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from habit_tracker.models import Habit
from habit_tracker.paginations import CustomPagination
from habit_tracker.serializers import HabitSerializer
from user.permissions import IsOwner


class HabitCreateAPIView(generics.CreateAPIView):
    """Создание привычки"""

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        habit = serializer.save()
        habit.user = self.request.user
        habit.save()


class HabitListAPIView(generics.ListAPIView):
    """Обзор привычек"""

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsOwner]
    pagination_class = CustomPagination


class HabitRetrieveAPIView(generics.RetrieveAPIView):
    """Изменения параметра привычки"""

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class HabitUpdateAPIView(generics.UpdateAPIView):
    """Апдейт привычки"""

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsOwner]


class HabitDestroyAPIView(generics.DestroyAPIView):
    """Удаление привычки"""

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class HabitPublishedListAPIView(ListAPIView):
    """Публичные привычки"""

    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination

    def get_queryset(self):
        """Фильтр для списка опубликованных привычек."""
        return Habit.objects.filter(is_published=True)
