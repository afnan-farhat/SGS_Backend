from django.db import models

class Department(models.Model):
    Dep_name = models.CharField(max_length=255, primary_key=True, db_column='Dep_name')
    Location = models.CharField(max_length=255, blank=True, db_column='Location')

    def __str__(self):
        return self.Dep_name

class Project(models.Model):
    P_ID = models.AutoField(primary_key=True, default=14)
    Project_title = models.CharField(max_length=200)
    Request_type = models.CharField(max_length=50)
    Drive = models.CharField(max_length=100)
    Objective = models.TextField()
    Scope = models.TextField()
    Requirements = models.TextField()
    Regulatory = models.CharField(max_length=100,blank=True)
    Priority = models.CharField(max_length=100)

    # Make all the rest optional
    Forwarded = models.BooleanField(default=False)
    Approved = models.BooleanField(default=False)
    Assigned = models.BooleanField(default=False)
    P_description = models.TextField(blank=True, null=True)
    P_state = models.CharField(max_length=100, blank=True, null=True)
    P_budget = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    P_budgeted = models.BooleanField(default=False)
    Progress = models.IntegerField(blank=True, null=True)
    Requestor = models.CharField(max_length=100, blank=True, null=True)
    Digital_strategy = models.BooleanField(default=False)
    Digitalization = models.BooleanField(default=False)
    P_start_date = models.DateField(blank=True, null=True)
    P_end_date = models.DateField(blank=True, null=True)
    Dep_name = models.CharField(max_length=100, blank=True, null=True)
    PRN = models.CharField(max_length=100, blank=True, null=True)
    type = models.CharField(max_length=100, default='Request')

    def __str__(self):
        return self.Project_title


class Employee(models.Model):
    PRN = models.AutoField(primary_key=True, db_column='PRN')
    Emp_name = models.CharField(max_length=255, db_column='Emp_name')
    Job_title = models.CharField(max_length=255, blank=True, db_column='Job_title')
    Email = models.EmailField(blank=True, db_column='Email')
    Chat = models.CharField(max_length=255, blank=True, db_column='Chat')
    Work_phone = models.CharField(max_length=50, blank=True, db_column='Work_phone')
    Buisness_address = models.CharField(max_length=255, blank=True, db_column='Buisness_address')
    Dep_name = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True, db_column='Dep_name')
    P_ID = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True, blank=True, db_column='P_ID')
    Employee_count = models.IntegerField(default=1, db_column='Employee_count')
    Grade = models.CharField(max_length=50, blank=True, db_column='Grade')
    Emp_role = models.CharField(max_length=50, db_column='Emp_role')

    def __str__(self):
        return self.Emp_name


class Stages(models.Model):
    Stages_ID = models.AutoField(primary_key=True, db_column='Stages_ID')
    Stage_name = models.CharField(max_length=100, db_column='Stage_name')
    Status = models.CharField(max_length=100, db_column='Status')
    S_start_date = models.DateField(db_column='S_start_date')
    S_end_date = models.DateField(db_column='S_end_date')
    S_progress = models.IntegerField(db_column='S_progress')
    P_ID = models.ForeignKey(Project, on_delete=models.CASCADE, db_column='P_ID')

    def __str__(self):
        return f"{self.Stage_name} (Project ID: {self.P_ID_id})"


class Task(models.Model):
    Task_ID = models.AutoField(primary_key=True, db_column='Task_ID')
    Task_name = models.CharField(max_length=100, db_column='Task_name')
    File = models.FileField(upload_to='tasks/', blank=True, null=True, db_column='File')
    Stages_ID = models.ForeignKey(Stages, on_delete=models.CASCADE, db_column='Stages_ID')

    def __str__(self):
        return self.Task_name
