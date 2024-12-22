from django.contrib import admin

from user.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_filter = ("id", "email")
    list_display = ("id", "email")
    search_fields = ("id", "email")
