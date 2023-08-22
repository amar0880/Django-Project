from django.shortcuts import render

# Create your views here.

def index_view(request):
    
    db={
        
        1:{'sr_no':1, "name": "Amar", 'course' : "Python", 'addre': "Pune" , 'testn' : " Django ", 'testm': 55},
        2:{'sr_no':2, "name": "Ashutosh",'course' : "Python", 'addre': "Pune" , 'testn' : " Django ", 'testm': 55},
        3:{'sr_no':3, "name": "Amruta" ,'course' : "Python", 'addre': "Pune" , 'testn' : " Django ", 'testm': 55},
        4:{'sr_no':4, "name": "Pratiksha", 'course' : "Python", 'addre': "Pune" , 'testn' : " Django ", 'testm': 55},
        5:{'sr_no':5, "name": "Rohit", 'course' : "Python", 'addre': "Pune" , 'testn' : " Django ", 'testm': 55},
        6:{'sr_no':6, "name": "Bhagyshree", 'course' : "Python", 'addre': "Pune" , 'testn' : " Django ", 'testm': 55},
        
    }
    context={'data':db}
    
    return render(request,'demoapp\index.html',context)