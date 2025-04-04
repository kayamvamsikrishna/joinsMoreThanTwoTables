from django.db import models

# Create your models here.
class Dept(models.Model):
    deptno=models.IntegerField(primary_key=True)
    dname=models.CharField(max_length=100)
    mgr=models.CharField(max_length=100,null=True, blank=True) 
    mname=models.CharField(max_length=100)

    def __str__(self):
       return str(self.deptno)
   
class Emp(models.Model):
    eno=models.CharField(max_length=100,primary_key=True)
    ename=models.CharField(max_length=100)
    hiredate=models.DateField(default='2000-09-20')#orm date formate 'yyyy-mm-dd'
    job=models.CharField(max_length=100)
    mgr=models.ForeignKey('self',on_delete=models.SET_NULL,null=True,blank=True)
    sal=models.FloatField(max_length=100)
    comm=models.FloatField(max_length=100)
    deptno=models.ForeignKey(Dept,on_delete=models.CASCADE)
    def __str__(self):
       return self.eno