from django.db import models

# Create your models here.
class Employee(models.Model):
    name= models.CharField(max_length=60)
    emails=models.EmailField(unique=True)
    age=models.IntegerField()
    salary=models.FloatField()
    department = models.ForeignKey(
        'Department',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='employees'
    )
    address=models.TextField(max_length=45,default='Null')
    company = models.ForeignKey(
    'Company',
    on_delete=models.CASCADE,
    related_name='employee',
    null=True,
    blank=True
)

    def __str__(self):
      return self.name

class Company(models.Model):
    name= models.CharField(max_length=60)
    emails=models.EmailField(unique=True)
    location=models.TextField(max_length=45,default='Null')
    branch_number=models.IntegerField()
   

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=60, unique=True)
    description = models.TextField(max_length=200, blank=True)

    def __str__(self):
        return self.name