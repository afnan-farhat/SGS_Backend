from django.db import models
from django.shortcuts import render


class UserProject(models.Model):
    P_ID = models.AutoField(primary_key=True)
    P_name = models.CharField(max_length=255)
    P_description = models.TextField()
    P_state = models.CharField(max_length=50)
    p_budget = models.DecimalField(max_digits=15, decimal_places=2)
    p_budgeted = models.BooleanField()
    progress = models.IntegerField()
    priority = models.CharField(max_length=50)
    requestor = models.CharField(max_length=255)
    digital_starategy = models.CharField(max_length=255)
    digitalization = models.BooleanField()
    p_start_date = models.DateField(db_column='p_start_date')
    p_end_date = models.DateField(db_column='p_end_date')
    Project_Manager = models.CharField(max_length=255)

    # request_ID = models.IntegerField()
    # dep_ID = models.IntegerField()
    regulator = models.CharField(max_length=255, blank=True, null=True)  # <-- Added this line


    class Meta:
        db_table = 'users_project'  # exactly as the MySQL table name
        managed = False            # Django won't manage the table creation or migrations

    def __str__(self):
        return self.P_name


from django.db import models

class Request(models.Model):
    request_ID = models.AutoField(primary_key=True)
    Project_title = models.CharField(max_length=255)
    requestType = models.CharField(max_length=255)
    Driver = models.CharField(max_length=255)
    objective = models.TextField()
    Scope = models.TextField()
    Requirments = models.TextField() 
    request_state = models.CharField(max_length=100)
    dep_ID = models.IntegerField()    

    def __str__(self):
        return self.Project_title





def dashboard_view(request):
    projects = Project.objects.all()

    # Calculate stats in Python, like counts by status, budgets, etc.
    status_counts = {}
    total_budget = 0
    for p in projects:
        status = p.P_state.lower() if p.P_state else 'unknown'
        status_counts[status] = status_counts.get(status, 0) + 1
        total_budget += p.budget if hasattr(p, 'budget') else 0

    context = {
        'projects': projects,
        'status_counts': status_counts,
        'total_budget': total_budget,
        # Add other processed data needed for charts
    }
    return render(request, 'dashboard.html', context)
