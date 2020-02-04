"""Job_Portal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

import Home.views
#import Sign_Up.views
#import Sign_In.views
import Drop_Cv.views
import Post_Job.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home.views.home,name='home'),
   # path('SignUp/', Sign_Up.views.sign_up,name='SignUp'),
    #path('SignIn/', Sign_In.views.sign_in,name='SignIn'),
    path('Resume/', Drop_Cv.views.resume,name='Resume'),
    path('PostJob/',Post_Job.views.PostJob,name='PostJob'),
    path('accounts/',include('accounts.urls')),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

