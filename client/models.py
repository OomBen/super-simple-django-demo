from django.db import models

# Remember to register a model in the admin.py file

# Create your models here.
class EmployeeTable(models.Model):
    Name = models.CharField(max_length=250)
    Surname = models.CharField(max_length=250)
    Birth_Date = models.DateField()
    Employee_Number = models.CharField(max_length=250)
    Salary = models.BigIntegerField()
    Role_Description = models.CharField(max_length=250)
    Reporting_Line = models.CharField(max_length=250)
    Reporting_person = models.CharField(max_length=250)

    def __str__(self):
        return str(self.Name)

    class Meta:
        ordering = ('-Salary',)
