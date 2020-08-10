from django.shortcuts import render,redirect
from django.http import HttpResponse
from App.models import StudentData
from App.forms import insert_Student

# Create your views here.
def stu_view(request):
    Student=StudentData.objects.all()
    my_dict={'Student':Student}
    return render(request,'App/home.html',context=my_dict)

def insert_view(request):
    form=insert_Student()
    if request.method=='POST':
        form=insert_Student(request.POST)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'App/insert.html',{'form':form})

def delete_view(request,id):
    stu=StudentData.objects.get(id=id)
    stu.delete()
    return redirect('/')

def update_view(request,id):
    stu=StudentData.objects.get(id=id)
    if request.method=='POST':
        form=insert_Student(request.POST,instance=stu)
        if form.is_valid():
            form.save()
            print("data update**********")
        return redirect('/')
    return render(request,'App/update.html',{'stu':stu})
