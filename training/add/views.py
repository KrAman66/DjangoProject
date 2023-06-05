from django.shortcuts import render
from add.models import addition
# Create your views here.

def home(request):

    if(request.method=='GET'):
        return render(request,'add/intro.html')
    
    if(request.method=='POST'):
        name = request.POST['name']
        value1 = int(request.POST['val1'])
        value2 = int(request.POST['val2'])

        value3 = value1 + value2
        add = addition(name=name,input1=value1,input2=value2,sum_val=value3)
        add.save() 

        dic ={
            'value1':(value1),
            'value2':(value2),
            'value3':(value3),
            
        }
        return render(request,'add/sum.html',context=dic)
        
def display_con(request):

     additions = addition.objects.raw('select * from add_addition')
     return render(request,'add/display.html',{'addition':additions})


def database_src(request):
    if(request.method=='GET'):
        return render(request,'add/src_disp.html')

         
    if(request.method=='POST'):
        name=request.POST['name']
        add_check=addition.objects.raw('select * from add_addition where name="'+name+'"')
        if(len(add_check) == 0):
            msg='record not found'
            return render(request,'add/src_disp.html',{'msg':msg})
        else:
            return render(request,'add/display_con.html',{'add_check':add_check})
        