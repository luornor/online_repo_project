from multiprocessing import context
from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from .forms import  UploadFileForm, UserModelForm
from .models import UploadModel
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .decorators import unauthenticated_user,allowed_users




# Create your views here.
@unauthenticated_user
def signup(request):
    form = UserModelForm()

    if request.method == 'POST':
        form = UserModelForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            passwword = form.cleaned_data.get('username')

            group = Group.objects.get(name='students')
            user.groups.add(group)
            
            messages.success(request,'Account was successfuly created for '+ username)
            return redirect('user-login')
    
    context={'form':form}
    return render(request,'users/signup.html',context)


@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.warning(request, 'Username OR password is Incorrect')


    return render(request,'users/login.html')


def logoutUser(request):
    logout(request)
    return redirect('user-login')


@login_required(login_url='user-login')

def index(request):
    files = UploadModel.objects.all()
    
    context = {
        'files':files,
    }
    return render(request,'users/index.html',context)

@login_required(login_url='user-login')
@allowed_users(allowed_roles=['admin'])
def upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UploadFileForm()
  
    context = { 
            'form':form 
            }
    return render(request,'users/upload.html',context)

@login_required(login_url='user-login')
@allowed_users(allowed_roles=['admin'])
def delete_file(request,pk):
    if request.method == 'POST':
        files = UploadModel.objects.get(pk=pk)
        files.delete()
        return redirect('home')

    return render(request,'users/delete.html')


@login_required(login_url='user-login')
def student(request):
    
    return render(request,'users/student.html',context)

