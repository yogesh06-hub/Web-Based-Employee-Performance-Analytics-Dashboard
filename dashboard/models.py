from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    department = models.CharField(max_length=80)
    initials = models.CharField(max_length=4)
    color = models.CharField(max_length=7, default="#6D5DFB")
    performance_score = models.PositiveIntegerField()
    goals_completed = models.PositiveIntegerField(default=0)
    goals_total = models.PositiveIntegerField(default=1)
    attendance = models.PositiveIntegerField(default=100)
    status = models.CharField(max_length=20, default="On Track")

    class Meta:
        ordering = ["-performance_score"]

    def __str__(self):
        return self.name


class Goal(models.Model):
    class Status(models.TextChoices):
        NOT_STARTED = "Not started", "Not started"
        IN_PROGRESS = "In progress", "In progress"
        COMPLETED = "Completed", "Completed"

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="assigned_goals")
    title = models.CharField(max_length=180)
    target = models.PositiveIntegerField(help_text="Target value, such as 10 completed tasks.")
    progress = models.PositiveIntegerField(default=0, help_text="Current value achieved toward the target.")
    due_date = models.DateField()
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.NOT_STARTED)

    class Meta:
        ordering = ["due_date", "employee__name"]

    def __str__(self):
        return f"{self.employee.name}: {self.title}"
