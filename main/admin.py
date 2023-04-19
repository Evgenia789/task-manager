from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Tag, Task


class TaskManagerAdminSite(admin.AdminSite):
    pass


task_manager_admin_site = TaskManagerAdminSite(name="Task manager admin")


@admin.register(Tag, site=task_manager_admin_site)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name", "uniq_id")
    search_fields = ("name",)


@admin.register(Task, site=task_manager_admin_site)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "created_date",
        "updated_date",
        "deadline",
        "status",
        "priority",
        "author",
        "executor",
    )
    list_editable = ("status", "priority")
    list_filter = ("deadline", "status", "priority", "author", "executor")
    search_fields = ("name",)


@admin.register(User, site=task_manager_admin_site)
class UserAdmin(UserAdmin):
    list_display = ("first_name", "last_name", "role", "email")
    list_editable = ("role",)
