
from django.urls import path
from my_app import views

urlpatterns = [  

    path('admin_login', views.admin_login , name ='admin_login'),
    path('admin_index', views.admin_index , name ='admin_index'),
    path('about', views.about , name ='about'),
    path('insert', views.insertData , name ='insertData'),
    path('update/<id>', views.updateData , name ='updateData'),
    path('delete/<id>', views.deleteData , name ='deleteData'),
    path('admin_logout',views.admin_logout,name='admin_logout'),
    path('search',views.search,name='search'),



]