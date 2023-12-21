from django.shortcuts import render,redirect
from django.views.decorators.cache import never_cache
from .models import Users
from django.contrib import messages
from django.contrib import messages,auth
from django.http import HttpResponse
from django.views.decorators.cache import cache_control


# Create your views here.

@never_cache
def admin_login(request):
    
    if 'username' in request.session:
        return redirect(admin_index)
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.username == 'admin':
            request.session['username'] = username
            return redirect(admin_index)
        elif username!='admin':

            
            messages.info(request,'Invalid credentials.')
        else:
            messages.info(request, 'Invalid credentials.')
            # return redirect('admin_index')
    return render(request,"adminapp/admin_login.html")

@never_cache
def admin_index(request):
    data = Users.objects.all
    context={"data":data}
    return render(request,'adminapp/index.html',context)

@never_cache
def about(request):
    return render(request,'about.html')
@never_cache
def insertData(request):
    details = Users.objects.all
    context = {"details":details}
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        print(username,email,password)
        query = Users(username=username,email=email,password=password)
        query.save()
        messages.info(request,"Data Inserted Successfully")
        return redirect("admin_index")

    return render(request,'index.html',context)
@never_cache
def updateData(request,id):

    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
       
        edit = Users.objects.get(id=id)
        edit.username=username
        edit.email=email
        edit.password=password
        edit.save()
        messages.warning(request,"Data Updated Successfully")

        return redirect("admin_index")

    obj = Users.objects.get(id=id)
    context={"obj":obj}
    return render(request,'adminapp/edit.html',context)

@never_cache
def deleteData(request,id):
    d = Users.objects.get(id=id)
    d.delete()
    messages.error(request,"Data Deleted Successfully")

    return redirect("admin_index")

@never_cache
def search(request):
    if 'search' in request.GET:
        search = request.GET['search']
        data = Users.objects.all()
        context = {
            'data': data
        }
        if (Users.objects.filter(username__icontains=search)).exists():
            data = Users.objects.filter(username__icontains=search)
            context = {
                'data': data
            }
            return render(request, "adminapp/index.html", context)
        else:
            return HttpResponse('NO RESULT FOUND!')

    return render(request, "adminapp/index.html",context)

@never_cache
def admin_logout(request):
    if 'username' in request.session:
        request.session.flush()
    return redirect('admin_login')
    