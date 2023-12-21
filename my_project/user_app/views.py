from django.shortcuts import render,redirect
from django.contrib import messages
from my_app.models import Users
from django.contrib import messages,auth
from django.views.decorators.cache import never_cache

# Create your views here.


@never_cache
def log(request):
    if 'username' in request.session:
        return redirect(index)
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        if Users.objects.filter(username=username, password=password).exists():
            request.session['username'] = username
            return redirect(index)
        else:
            messages.error(request,'invalid username and password')
            return render(request, 'sampleapp/log.html')
    return render (request,'sampleapp/log.html')

@never_cache
def reg(request):
    if request.method=='POST':
        email=request.POST.get('email')
        username=request.POST.get('username')
        password=request.POST.get('password')
        conpassword=request.POST.get('conpassword')
        if password != conpassword:
            messages.info(request,'password is not maching')
        if Users.objects.filter(username=username).exists():
            messages.info(request,'Username is already exists')
        if Users.objects.filter(email=email).exists():
            messages.info(request,'email is taken.')
        
        new_user=Users(username=username,email=email,password=password)
        new_user.save()
        return redirect(log)
    
    return render (request,'sampleapp/reg.html')


@never_cache
def index(request):
    if 'username' in request.session:
        username=request.session['username']
        return render(request,"sampleapp/index.html",{'username':username})
    return redirect(log)

@never_cache
def logout(request):
    if 'username' in request.session:
        request.session.flush()
    return redirect(log)