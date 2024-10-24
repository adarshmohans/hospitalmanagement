from django.db import models

# Create your models here.

class Department(models.Model):
    dept_name = models.TextField(max_length=50)
    dept_desc = models.TextField(max_length=350)
    
    def __str__(self) :
        return self.dept_name
    
class Doctor(models.Model):
    doc_name = models.CharField(max_length=50)
    doc_dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    doc_img = models.ImageField(upload_to='doctors/')
    
    def __str__(self) :
        return self.doc_name
    
class Booking(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=15)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    booked = models.DateField()
    time = models.TimeField()
    desc = models.TextField(max_length=500)
    
    def __str__(self) :
        return self.name
    