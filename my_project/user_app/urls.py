from django.urls import path
from user_app import views

urlpatterns = [

    path('', views.index , name ='index'),
    path('log/',views.log,name='log'),
    path('reg/',views.reg,name='reg'),
    path('logout/', views.logout, name='logout'), 



 
]