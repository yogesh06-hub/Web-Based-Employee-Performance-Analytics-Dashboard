from django.shortcuts import render
from .models import Employee

DEMO_EMPLOYEES = [
    ("Aarav Sharma", "Senior Product Designer", "Design", "AS", "#7257E8", 96, 8, 9, 98, "Exceeding"),
    ("Maya Patel", "Marketing Manager", "Marketing", "MP", "#FF8A6B", 92, 7, 8, 96, "Exceeding"),
    ("Daniel Chen", "Software Engineer", "Engineering", "DC", "#3BAFA0", 89, 6, 8, 94, "On Track"),
    ("Sofia Williams", "HR Specialist", "People", "SW", "#F0B64D", 86, 7, 9, 97, "On Track"),
    ("Noah Johnson", "Data Analyst", "Analytics", "NJ", "#4B8DEB", 82, 5, 7, 92, "On Track"),
    ("Emma Brown", "Sales Executive", "Sales", "EB", "#E95D9B", 76, 5, 8, 90, "Needs Support"),
]


def dashboard(request):
    if not Employee.objects.exists():
        Employee.objects.bulk_create([Employee(name=n, role=r, department=d, initials=i, color=c, performance_score=s, goals_completed=g, goals_total=t, attendance=a, status=st) for n, r, d, i, c, s, g, t, a, st in DEMO_EMPLOYEES])
    employees = list(Employee.objects.all())
    avg_score = round(sum(e.performance_score for e in employees) / len(employees))
    context = {
        "employees": employees,
        "avg_score": avg_score,
        "on_track": sum(1 for e in employees if e.status != "Needs Support"),
        "goal_rate": round(sum(e.goals_completed for e in employees) / sum(e.goals_total for e in employees) * 100),
        "remaining_rate": 100 - round(sum(e.goals_completed for e in employees) / sum(e.goals_total for e in employees) * 100),
        "chart_scores": [e.performance_score for e in employees],
        "chart_names": [e.name.split()[0] for e in employees],
    }
    return render(request, "dashboard/index.html", context)
