from django.shortcuts import render
from app1.models import *
from django.db.models import Q
# Create your views here.
def joinMoreThanTwoTables(request):
    
    #WO=Emp.objects.all().select_related('deptno','mgr')
    #WO=Emp.objects.all().select_related('deptno','mgr').filter(ename='HARSHAD')
    #WO=Emp.objects.all().select_related('deptno','mgr').order_by('sal')[1:2:]
    #WO=Emp.objects.all().select_related('deptno','mgr').order_by('sal')[:1]
    #WO=Emp.objects.all().select_related('deptno','mgr').order_by('-sal')[1:2:]
    #WO=Emp.objects.all().select_related('deptno','mgr').order_by('-sal')[:1]
    #WO=Emp.objects.all().select_related('deptno','mgr').filter(deptno__dname='OWNER')#FILTER CONDITION BASED ON PARENT COLUMN DATA
    #AND operator
    #WO=Emp.objects.all().select_related('deptno','mgr').filter(Q(sal__gt=75000) & Q(sal__lt=200000) ).order_by('sal')
    #WO=Emp.objects.all().select_related('deptno','mgr').filter(Q(sal__gt=75000) & Q(sal__lt=200000) ).order_by('sal')
    
    #HARSHAD'S MANAGER'S MANAGER DETAILS USING ORM (join the emp table & dept table)
    WA=Emp.objects.get(ename='HARSHAD')#TAKE THE HARSHAD RECORDS INTO AN OBJECT
    PP=WA.mgr#EXTRACT HARSHAD'S MGR   
    WP=Emp.objects.get(eno=PP)#TAKE VAMSIKRISHNA RECORD BASED ON HARSHAD'S MGR (HARSHAD'S MGR==VAMSIKRISHNA'S ECODE)
    P=WP.mgr #EXTRACT VAMSIKRISHNA'S MGR
    WO=Emp.objects.all().select_related('deptno','mgr').filter(eno=P)#TAKE GREESHMA RECORD BASED ON VAMSIKRISHNA'S MGR (VAMSIKRISHNA'S MGR==GREESHMA'S ECODE)
    
    
    
    
    DD={'WO':WO}
    return render(request,'h1.html',DD)
    
    '''
    WO=Emp.objects.all().select_related('mgr')
    DD={'WO':WO}
    return render(request,'h2.html',DD)
    '''