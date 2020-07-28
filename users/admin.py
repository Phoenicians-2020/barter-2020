from django.contrib import admin
from django.contrib.auth import get_user_model

from users.models import (
    Profile,
    Interests,
    User
)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "gender", ]
    search_fields = ["user__name", "user__email"]


@admin.register(Interests)
class InterestsAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "date_created", "date_updated"]
    search_fields = ["name"]


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["id", "username", "name", "is_superuser"]
    search_fields = ["name"]
