from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from demo.models import Student
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def home(request):

    if(request.method=='GET'):
        return render(request,'demo/intro.html')

    if(request.method=='POST'):
        name = request.POST['name']
        roll = request.POST['roll']
        mark = request.POST['mark']

        #lets verify
        checkStudExist = Student.objects.raw('select * from demo_student where name ="'+name+'"')

        if len(checkStudExist) > 0:
            dict={
                'msg': 'Record exist'
            }
            return render(request,'demo/intro.html', context=dict)
        else:
            stud_info = Student(name=name, roll=roll, mark=mark)
            stud_info.save()
            dict = {
              'msg':'Record Saved'
            }
            return render(request,'demo/intro.html',context=dict)


@login_required
def display(request):

    students = Student.objects.raw('select*from demo_student')
    return render(request,'demo/display.html',{'students':students})


@login_required
def update(request,id):
    if(request.method=='POST'):
       id = request.POST['id']
       mark = request.POST['mark']
       roll = request.POST['roll']
       Student.objects.filter(id=id).update(mark=mark)
       return redirect('show')
    else:
       get_student = Student.objects.get(id=id)
       return render(request,'demo/update.html',{'get_student':get_student})


@login_required
def delete(request,id):
     get_student = Student.objects.get(id=id)
     get_student.delete()
     return redirect('show')      