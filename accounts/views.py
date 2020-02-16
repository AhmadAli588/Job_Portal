from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth


def signup(request):
    if request.method=='POST':

        username=request.POST['username']
        email = request.POST['Uemail']
        Password = request.POST['pass']
        RepeatPass = request.POST['re_pass']
        if Password==RepeatPass:
            if User.objects.filter(username=username).exists():
                return render(request, 'accounts/Sign_Up.html', {'error': 'username already taken'})
            elif User.objects.filter(email=email).exists():
                return render(request, 'accounts/Sign_Up.html', {'error': 'Email already taken'})
            else:
                user=User.objects.create_user(request.POST['username'],request.POST['Uemail'],request.POST['pass'])
                #auth.login(request, user)
                user.save()
                return redirect('signin')
        else:
            return render(request, 'accounts/Sign_Up.html', {'error': 'Password Does NOt Match'})
    else:
        return render(request, 'accounts/Sign_Up.html')


def signin(request):
    if request.method=='POST':
        user=auth.authenticate(username=request.POST['your_name'],password=request.POST['your_pass'])
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            return render(request, 'accounts/Sign_In.html',{'error': 'username or password incorrect '})
    else:
        return render(request,'accounts/Sign_In.html')

def logout(request):
    if request.method=='POST':
        auth.logout(request)
        return redirect('home')
    return render(request,'accounts/Sign_Up.html')

