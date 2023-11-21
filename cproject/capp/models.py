from django.db import models

# Create your models here.
class Department(models.Model):
    d_name = models.CharField(max_length=50)

    def __str__(self):
        return self.d_name


class Course(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    c_name = models.CharField(max_length=50)

    def __str__(self):
        return self.c_name

class Material(models.Model):
    m_name = models.CharField(max_length=50)

    def __str__(self):
        return self.m_name

class Student(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=15)
    mail_id = models.EmailField()
    address = models.TextField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    purpose = models.CharField(max_length=50)
    materials_provide = models.ManyToManyField(Material)

    def __str__(self):
        return self.name
