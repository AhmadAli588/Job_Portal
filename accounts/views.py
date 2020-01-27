from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
def signup(request):
    if request.method=='POST':
       # First_Name=request.POST['FirstName']
       # Second_Name=request.POST['SecondName']
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
                auth.login(request, user)
                user.save()
                return redirect('home')
        else:
            return render(request, 'accounts/Sign_Up.html', {'error': 'Password Does NOt Match'})
    else:
        return render(request, 'accounts/Sign_Up.html')







    #if request.method == 'POST':

        # User has info and wants an account now!

     #   if request.POST['pass'] == request.POST['re_pass']:

      #      try:

       #         user = User.objects.get(username=request.POST['name'])
        #        user_email = User.objects.get(user_email=request.POST['email'])
         #       return render(request, 'accounts/signup.html', {'error': 'Username has already been taken'})

          #  except User.DoesNotExist:

           #     user = User.objects.create_user(request.POST['name'], user_email=request.POST['email'],password=request.POST['pass'])

            #    auth.login(request, user)

             #   return redirect('home')

        #else:

         #   return render(request, 'accounts/Sign_Up.html', {'error': 'Passwords must match'})

    #else:

        # User wants to enter info

     #   return render(request, 'accounts/Sign_Up.html')



    #if request.method=="POST":
     #   if request.POST['pass']==request.POST['re_pass']:
      #      try:
       #         user=User.objects.get(username=request.POST['name'])
        #        user_email=User.objects.get(user_email=request.POST['email'])
         #       return render(request,'accounts/signup.html',{'error':'username and email already taken'})
          #  except User.DoesNotExist:
           #     user=User.objects.create_user(request.POST['username'],user_email=request.POST['email'],password=request.POST['pass'])
            #    auth.login(request,user)
             #   return redirect('home')
    #else:
     #   return render(request, 'accounts/Sign_Up.html')






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

