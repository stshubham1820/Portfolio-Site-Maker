from django.http.response import HttpResponse, HttpResponseRedirect
from django.db.utils import IntegrityError
from django.shortcuts import redirect, render
from port.models import *
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.models import User
# Create your views here.

def info(request):
    if request.method == "POST":
        if request.POST.get("userName"):
            print("LogPOST")
            uname = request.POST.get('userName')
            passw = request.POST.get('password')
            user = authenticate(request,username=uname,password=passw)
            print(user)
            try:
                if user is not None:
                    login(request,user)
                    request.session['uname']=uname#creating Session
                    try:
                        user_profile.objects.get(user_name=uname)
                        url = '/dashboard/?uname={}'.format(uname)
                        return HttpResponseRedirect(url)
                    except user_profile.DoesNotExist:
                        url = '/dashboard/?uname={}'.format(uname)
                        return HttpResponseRedirect(url)
                elif user is None :
                    messages.info(request,"Enter Valid Username / Password")
                    return render(request,'login.html')      
            except User.DoesNotExist:
                messages.info(request,"User is Not Here")
                return render(request,'login.html')
        elif request.POST.get("RuserName"):
            print("SignUp")
            uname = request.POST.get('RuserName')
            passw = request.POST.get('Rpassword')
            Email = request.POST.get('REmail')
            if uname == "" and passw == "":
                return render(request,'login.html')
            else:
                user = authenticate(request,username=uname,password=passw)
                try:
                    if user is not None:
                        messages.info(request,"User is Already Here")
                        return render(request,'login.html')
                    else :
                        try :
                            print("except")
                            user = User(username=uname,password=passw,email=Email)
                            user.set_password(passw)
                            user.is_staff = False
                            user.is_superuser = False
                            user.save()
                            print("Save",user)
                            messages.success(request,"Registration Sucessful")
                            return render(request,'login.html')
                        except IntegrityError:
                            request.session['uname']="null"
                            return render(request,'login.html')
                except User.DoesNotExist:
                    messages.info(request,"User is Not Here")
                    return render(request,'login.html')              
    else :
        return render(request,'login.html')
    messages.info(request,"Username & Password is Empty")
    return render(request,'login.html')
def Logout(request):
    user = request.session['uname']
    print(user)
    logout(request)
    request.session['uname']="null"
    print(request.session['uname'])
    url = '/'
    response = HttpResponse(url)
    response['Age'] = 120
    response['Cache-Control'] = 'no-cache, must-revalidate'
    response['Expires'] = 'Sat, 26 Jul 1997 05:00:00 GMT'
    return response
