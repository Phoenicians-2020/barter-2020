from django.contrib import admin
from django.contrib.auth import get_user_model

from users.models import User, Profile


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["username", "name", "is_superuser"]
    search_fields = ["name"]


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "gender", ]
    search_fields = ["user__name", "user__email"]
