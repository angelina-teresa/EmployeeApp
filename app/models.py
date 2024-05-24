from django.db import models

class Employee(models.Model):  
    eid = models.CharField(max_length=20)  
    ename = models.CharField(max_length=100)  
    eemail = models.EmailField()  
    econtact = models.CharField(max_length=15)  
    class Meta:  
        db_table = "employee"

class Department(models.Model):
    did = models.CharField(max_length=255)
    ename = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'department'