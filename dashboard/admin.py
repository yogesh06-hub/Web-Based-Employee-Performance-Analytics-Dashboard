from django.contrib import admin
from .models import Employee, Goal


class GoalInline(admin.TabularInline):
    model = Goal
    extra = 1
    fields = ("title", "target", "progress", "due_date", "status")


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("name", "role", "department", "performance_score", "goals_completed", "goals_total", "attendance", "status")
    list_filter = ("department", "status")
    search_fields = ("name", "role", "department")
    ordering = ("name",)
    inlines = [GoalInline]
    fieldsets = (
        ("Employee profile", {"fields": ("name", "role", "department", "initials", "color")}),
        ("Quarterly performance", {"fields": ("performance_score", "attendance", "status")}),
        ("Goal summary", {"fields": ("goals_completed", "goals_total")}),
    )


@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    list_display = ("title", "employee", "progress", "target", "due_date", "status")
    list_filter = ("status", "due_date")
    search_fields = ("title", "employee__name")
    autocomplete_fields = ("employee",)
