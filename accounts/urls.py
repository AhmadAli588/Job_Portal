from django.urls import path,include
from . import views
urlpatterns = [
    path('signup/', views.signup,name='signup'),
    path('signin/', views.signin,name='signin'),
    path('logout/', views.logout,name='logout'),
]
#urlpatterns=[
 #   url(r'login/$',auth_views.LoginView.as_view(template_name='accounts/Sign_IN.html'),name='login'),
  #  url(r'logout/$',auth_views.LogoutView.as_view(),name='logout'),
   # url(r'signup/$',views.SignUp.as_view(),name='signup')
#]