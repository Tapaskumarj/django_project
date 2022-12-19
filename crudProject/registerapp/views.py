from django.shortcuts import render,redirect
from .forms import studentForm
from django.contrib import messages
from .models import crud_student

# Create your views here.
def add(request):
    if request.method=='POST':
        fm=studentForm(request.POST)
        if fm.is_valid():
            messages.success(request, 'Data inserted successfully')
            fm.save()
            #fm = studentForm()
            return redirect('/show')
    else:
        fm=studentForm()
    return render(request, 'add.html', {'form':fm})

def show(request):
    users=crud_student.objects.all()
    return render(request,'show.html',{'users':users})

def delete(request,id):
    user=crud_student.objects.get(pk=id)
    user.delete()
    return redirect('/show')

def edit(request,id):
    users=crud_student.objects.get(pk=id)
    fm = studentForm(instance=users)
    return render(request,'edit.html',{'user':users,'form':fm})

def update(request,id):
    if request.method=='POST':
        users = crud_student.objects.get(pk=id)
        fm=studentForm(request.POST,instance=users)
        if fm.is_valid():
            fm.save()
            return redirect('/show')
    else:
        users = crud_student.objects.get(pk=id)
        fm = studentForm( instance=users)

    return render(request, 'edit.html',{'form':fm})

print("hello dude")

