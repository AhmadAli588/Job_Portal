from django.shortcuts import render,redirect
from django.utils import timezone
from .models import Post
from django.contrib.auth.decorators import login_required

@login_required(login_url="/accounts/signin/")
def PostJob(request):
    if request.method=='POST':
        if request.POST['full_name'] and request.POST['email'] and request.POST['detail'] and request.FILES['file']:
            post_m=Post()
            post_m.id=2
            post_m.full_name=request.POST['full_name']
            post_m.email=request.POST['email']
            post_m.detail=request.POST['detail']
            post_m.file=request.FILES['file']
            post_m.pub_date=timezone.datetime.now()
            post_m.recuiter=request.user
            post_m.save()
            return redirect('PostJob')
        else:
            return render(request,'Post_Job/Post_Job.html', {'error': "All Field Required"})
    else:
        return render(request,'Post_Job/Post_Job.html')

