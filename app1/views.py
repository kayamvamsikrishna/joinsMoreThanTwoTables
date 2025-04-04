from django.shortcuts import render
from app1.models import *
from django.db.models import Q
from django.db.models import Max,Avg,Min,Sum,Count,Prefetch
from django.db.models.functions import Length
# Create your views here.
def joinMoreThanTwoTables(request):
    #to fetch null values syntax: colName__isnull=True
     #WO=Emp.objects.all().select_related('deptno').filter(mgr__isnull=True)

    #to fetch except null values syntax: colName__isnull=False
    #WO=Emp.objects.all().select_related('deptno').filter(mgr__isnull=False)
    
    #to fetch that particular column starts with that particular char or not
    #WO=Emp.objects.all().select_related('deptno').filter(ename__startswith='H')




    #Difference between bellow two quaries
    #WO=Emp.objects.all().select_related('deptno')#here we had mgr object
    #WO=Emp.objects.all().select_related('deptno','mgr')







    #WO=Emp.objects.all().select_related('deptno').filter(job='CEO')
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





    #To fetch Max,Min,Count,Sum,Avg we aggregate method 
    #WO=Emp.objects.aggregate(Max('sal'))
    #print(WO)# aggregate method returns dictionary  example: {'sal__max': 200000.0}
    #WO=Emp.objects.aggregate(Min('sal'))
    #print(WO)# aggregate method returns dictionary  example: {'sal__min': 75000.0}
    #WO=Emp.objects.aggregate(Count('ename'))
    #print(WO)# aggregate method returns dictionary  example:{'ename__count': 6}
    #WO=Emp.objects.aggregate(Avg('sal'))
    #print(WO)# aggregate method returns dictionary  example:{'sal__avg': 104166.66666666667}

    #WO=Emp.objects.aggregate(ass=Avg('sal'))
    #print(WO)

    
    #WO=Emp.objects.aggregate(sss=Sum('sal'))#{'sss': 625000.0}
    #print(WO)
    #WO=Emp.objects.filter(deptno=1001).aggregate(avv=Avg('sal'))#{'avv': 85000.0}
    #print(WO)

    WO=Emp.objects.values('deptno').annotate(avv=Avg('sal')) #QuerySet [{'deptno': 1001, 'avv': 85000.0}, {'deptno': 1002, 'avv': 200000.0}] #annotate is used for grouping the data
    #if i use annotate method then the syntax is values('columnName').annotate(condition)
    print(WO)





   
    







    
    
   



    











    
    #HARSHAD'S MANAGER'S MANAGER DETAILS USING ORM (join the emp table & dept table)

    '''
    WA=Emp.objects.get(ename='HARSHAD')#TAKE THE HARSHAD RECORDS INTO AN OBJECT
    PP=WA.mgr#EXTRACT HARSHAD'S MGR   
    WP=Emp.objects.get(eno=PP)#TAKE VAMSIKRISHNA RECORD BASED ON HARSHAD'S MGR (HARSHAD'S MGR==VAMSIKRISHNA'S ECODE)
    P=WP.mgr #EXTRACT VAMSIKRISHNA'S MGR
    WO=Emp.objects.all().select_related('deptno','mgr').filter(eno=P)#TAKE GREESHMA RECORD BASED ON VAMSIKRISHNA'S MGR (VAMSIKRISHNA'S MGR==GREESHMA'S ECODE)
    '''
    
    #WO=Emp.objects.raw('select * from app1_Emp')
    #WO=Emp.objects.raw('select * from app1_Emp where ename="HARSHAD"')
    #WO=Emp.objects.all().select_related('deptno').filter(ename='VAMSIKRISHNA')
    

    
    
    
    DD={'WO':WO}
    return render(request,'h1.html',DD)
    
    '''
    WO=Emp.objects.all().select_related('mgr')
    DD={'WO':WO}
    return render(request,'h2.html',DD)
    '''
def updationMethods(request):
    #Update Method
    WO=Emp.objects.all().filter(Q(sal__gt=60000) & Q(sal__lt=80000)).update(ename='DHRUVA')
    WO=Emp.objects.all().filter(sal=75000).update(ename='PRANAY')
    WO=Emp.objects.filter(sal=100000).update(ename='VAMSIKRISHNA')
    WO=Emp.objects.all().filter(job='CEO').update(ename='GREESHMA')
    WO=Emp.objects.filter(comm=10000).update(ename='KISHORE')
    WO=Emp.objects.all().filter(Q(comm=60000) & Q(sal=80000)).update(ename='DHRUVA')
    WO=Emp.objects.all().filter(ename='VAMSIKRISHNA').update(deptno='1001')#While we are dealing with parent column(foreigh key columb)  that data should be definetly present in the parent column data
    WO=Emp.objects.all()

    #note: in the above statements it will only do updation but it does not create any new records or data




    #Update_or_create Method
    #WO=Emp.objects.all().filter(Q(sal__gt=60000) & Q(sal__lt=80000)).update_or_create(ename='PRANAY',defaults={'ename':'VAMSI'})
    #WO=Emp.objects.all().filter(sal=75000).update_or_create(ename='PRANAY',defaults={'ename':'VAMSI'})
    #WO=Emp.objects.filter(sal=100000).update_or_create(ename='VAMSIKRISHNA',defaults={'ename':'VAMSI'})
    #WO=Emp.objects.all().filter(job='CEO').update_or_create(ename='GREESHMA',defaults={'ename':'VAMSI'})
    #WO=Emp.objects.filter(comm=10000).update_or_create(ename='KISHORE',defaults={'ename':'VAMSI'})
    #WO=Emp.objects.all().filter(Q(comm=60000) & Q(sal=80000)).update_or_create(ename='DHRUVA',defaults={'ename':'VAMSI'})
    '''
    C=Emp.objects.get(deptno='1002')
    cc=C.deptno
    WO=Emp.objects.all().filter(ename='VAMSIKRISHNA').update_or_create(deptno=1001,defaults={'deptno':cc})#While we are dealing with parent column(foreigh key columb)  that data should be definetly present in the parent column data and we need to provide parent instance
    WO=Emp.objects.all()
    '''

    '''
    C=Emp.objects.get(deptno='1002')
    cc=C.deptno
    #WO=Emp.objects.all().filter(ename='VAMSIKRISHN').update_or_create(deptno=1001,defaults={'eno':2007,'sal':0,'comm':0,'deptno':cc})#While we are dealing with parent column(foreigh key columb)  that data should be definetly present in the parent column data and we need to provide parent instance
    #in the above primary key is mandatory,parent column data and it's instance is mandatory,....
    #sal and comm i need specify values because in models.py file i'm not created default vakues 'null=True blank=True' for both sal and comm columns 
    WO=Emp.objects.all()

    '''

    '''
    #DELETION OF PARTICULAR RECORD
    WO=Emp.objects.filter(comm=20).delete()
    WO=Emp.objects.all().delete()#It is used to delete all the records in the table 
    WO=Emp.objects.all()

    '''

    #note: if data is not there it create the data and in that case we need to provide that particular parent column instance also
    #it does not update multiple records

     



    DD={'WO':WO}
    return render(request,'h3.html',DD)




def prefetchR(request):
    #WO=Dept.objects.prefetch_related('emp_set').all()
    #Only Particular Dept and all the Employees
    #WO=Dept.objects.prefetch_related('emp_set').filter(dname='CYBER SECURITY')

    #Below Query gives Error
    #WO=Dept.objects.prefetch_related('emp_set').filter(emp_set__ename='GREESHMA')

    #Below quary is the correct representation of the above query
    WO=Dept.objects.prefetch_related(Prefetch('emp_set',queryset=Emp.objects.filter(ename='GREESHMA')))

    



    dD={'WO':WO}
    return render(request,'h4.html',dD)





