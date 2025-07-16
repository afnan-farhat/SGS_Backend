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
    p_start_date = models.DateField()
    p_end_date = models.DateField()
    request_ID = models.IntegerField()
    dep_ID = models.IntegerField()

    class Meta:
        db_table = 'users_project'  # exactly as the MySQL table name
        managed = False            # Django won't manage the table creation or migrations

    def __str__(self):
        return self.P_name


class Request(models.Model):
    Request_ID = models.AutoField(primary_key=True)
    Project_Title = models.CharField(max_length=255, default='Untitled Project')
    requestType = models.CharField(max_length=255, default='General')  # note lowercase r
    Driver = models.CharField(max_length=255, default='N/A')
    Requirments = models.TextField(default='None')
    Objective = models.TextField(default='No Objective')
    Scope = models.CharField(max_length=255, default='General Scope')
    request_state = models.CharField(max_length=50, default='waiting')
    dep_ID = models.IntegerField(default=0)

    class Meta:
        db_table = 'users_request'

    def __str__(self):
        return self.Project_Title
