from django.urls import path

from habit_tracker.apps import HabitTrackerConfig

from .views import (HabitCreateAPIView, HabitDestroyAPIView, HabitListAPIView,
                    HabitPublishedListAPIView, HabitRetrieveAPIView,
                    HabitUpdateAPIView)

app_name = HabitTrackerConfig.name


urlpatterns = [
    path("habit/create/", HabitCreateAPIView.as_view(), name="habit_create"),
    path("habit/list/", HabitListAPIView.as_view(), name="habit_list"),
    path(
        "habit/<int:pk>/retrieve/",
        HabitRetrieveAPIView.as_view(),
        name="habit_retrieve",
    ),
    path("habit/<int:pk>/update/", HabitUpdateAPIView.as_view(), name="habit_update"),
    path("habit/<int:pk>/delete/", HabitDestroyAPIView.as_view(), name="habit_delete"),
    path(
        "habit_published/", HabitPublishedListAPIView.as_view(), name="habit_published"
    ),
]
