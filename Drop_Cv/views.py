from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .models import Resume
from .forms import ResumeForm


@login_required(login_url="/accounts/signin")
def resume(request):
    if request.method=='POST':
        if request.POST['full_name'] and request.POST['email'] and request.POST['message'] and request.FILES['file']:
            resume_m=Resume()

            resume_m.full_name=request.POST['full_name']
            resume_m.email=request.POST['email']
            resume_m.message=request.POST['message']
            resume_m.file=request.FILES['file']
            resume_m.save()
            return redirect('Resume')
        else:
            return render(request, 'Drop_Cv/Rusme.html', {'error': "All Field Required"})
    else:
        return render(request, 'Drop_Cv/Rusme.html')












