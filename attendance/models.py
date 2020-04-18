from django.db import models

# Create your models here.
class Student(models.Model):
    student_name= models.CharField(max_length=200)
    register_no= models.IntegerField(default=5119)
    dob=models.DateTimeField('date of birth')
    def __str__(self):
        return self.student_name

    
class att(models.Model):
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    date=models.DateField('')
    period=models.IntegerField()
    present=models.BooleanField()
    def value(self):
        return self.present