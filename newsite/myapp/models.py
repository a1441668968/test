from django.db import models


# Create your models here.
class Department(models.Model):
    dep_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.dep_name


class Employee():
    emp_name = models.CharField(max_length=20)
    emp_phone = models.CharField(max_length=11)
    department = models.ForeignKey(Department, models.CASCADE)

    def __str__(self):
        return self.emp_name
