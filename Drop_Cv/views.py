from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth
from .models import Resume
from .forms import ResumeForm

def resume(request):
    if request=='POST':
        name=request.POST['full_name'];
        mail=request.POST['email'];
        body=request.POST['message'];
        Image=request.POST['file'];

        data=Resume(full_name=name,email=mail,message=body,file=Image)
        data.save()
        return render(request,'Drop_Cv/Rusme.html', {'messge':"Register"})


    else:
        return render(request, 'Drop_Cv/Rusme.html')



#def resume(request):
#    if request=='POST':
#        Full_name=request.POST['full_name']
#        Email=request.POST['email']
#        Message=request.POST['message']
#        File=request.POST['file']

#        object1=Resume(full_name=Full_name,email=Email,message=Message,file=File)
#        object1.save()
#        return render(request, 'Drop_Cv/Rusme.html',{'message':'Inserted'})
#    else:
#        return render(request,'Drop_Cv/Rusme.html')

#def resume(request):
#    if request=="POST":
#        form=ResumeForm(request.POST or None,request.FILES or None)
#        if form.is_valid():
#            f=form.save()
#            f.save()
#            form=ResumeForm()
#            return render(request,'Drop_Cv/Rusme.html', {'error':'inserted'})
#    return render(request,'Drop_Cv/Rusme.html')


#def Resume(request):
 #       if request.method=="POST":
  #              form=ResumeForm(request.POST)
   #             if form.is_valid():
    #                    form.save()
     #           else:
      #                  return render(request, 'Drop_Cv/Rusme.html',{'error': "Form is not valid" })
                #if form.is_valid():
                #FullName=request.POST['full_name']
                #Email=request.POST['email']
                #Message=request.POST['message']
                #File=request.POST['file']
                #instance=form.save(request.POST['full_name'],request.POST['email'],request.POST['message'])
                #instance.save()
                #messages.sucess(request,"Sucessfully inserted")
                #return render(request, 'Drop_Cv/Rusme.html')
                #return HttpResponseRedirect(instance.get_absolute_url())

                #else:
                 #       return render(request, 'Drop_Cv/Rusme.html',{'error': "Form is not valid" })

       # form = ResumeForm()
        #return render(request, 'Drop_Cv/Rusme.html')










