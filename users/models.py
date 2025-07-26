from django.db import models
from django.shortcuts import render
from django.db import models

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


class Employee(models.Model):
    Emp_ID = models.AutoField(primary_key=True)
    Emp_name = models.TextField()
    job_title = models.TextField()
    email = models.EmailField(unique=True)
    chat = models.TextField()
    work_phone = models.TextField()
    buisness_address = models.TextField()
    Emp_role = models.TextField()

    class Meta:
        db_table = 'users_employee'  # exactly as the MySQL table name
        managed = False            # Django won't manage the table creation or migrations

    def __str__(self):
        return self.Emp_name

class Request(models.Model):
    request_ID = models.AutoField(primary_key=True)
    Project_title = models.CharField(max_length=255)
    requestType = models.CharField(max_length=255)
    Driver = models.CharField(max_length=255)
    objective = models.TextField()
    Scope = models.TextField()
    Requirments = models.TextField() 
    request_state = models.CharField(max_length=100)
    forwarded = models.BooleanField()
    approved = models.BooleanField()
    Assigned = models.BooleanField()
    dep_ID = models.IntegerField()    
    P_ID = models.ForeignKey(UserProject, on_delete=models.CASCADE, db_column='P_ID')
    

    def __str__(self):
        return self.Project_title



