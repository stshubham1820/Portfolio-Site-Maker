from django.http import HttpResponseRedirect , HttpResponse 
from django.shortcuts import redirect, render
from .models import *
from django.contrib import messages
from django.core.mail import send_mail
# Create your views here.
def dashboard(request):
    if request.session['uname']=="null":
        response = redirect('/')
        return response
    print(request.session['uname'])
    uname=request.GET.get('uname')
    if request.method == "GET":
        try :
            User = user_profile.objects.get(user_name=uname)
            User_abt = user_about.objects.get(user=uname)
            User_res = resume.objects.get(user=uname)
            Intrest = intrest.objects.all()
            Intrest = intrest.objects.filter(user=uname)
            Intrest = Intrest.order_by('intrest')
            Testimonial = testimonial.objects.filter(user=uname)
            Testimonial = Testimonial.order_by('ClientName')
            Services = Service.objects.filter(user=uname)
            Services = Services.order_by('ServiceName')
            Image = Images.objects.filter(User=uname)
            UEmail = User_abt.email
            skills = User_res.skill
            skills = skills.split(",")
            var1 = skills
            skillsper = User_res.skillpercentage
            skillsper = skillsper.split(",")
            List = []
            for i in Image:
                List.append(i.Category)
            List.sort()
            cat = set(List)
            cat = sorted(cat)
            print(cat)
            Dict = zip(var1,skillsper)
            return render(request,'dashboard_user.html',{'user':uname,'User':User,'Userabt':User_abt,
            'Userres':User_res,'Dict':Dict,'Intrest':Intrest,'Testimonial':Testimonial,
            'Services':Services,'Images':Image,'Category':cat,'Done':""})
        except user_profile.DoesNotExist:
            messages.info(request,"Your Site is Not Ready Please Fill the Form to get a Site Link")
            return render(request,'dashboard_unuser.html',{'user':uname})
        except user_about.DoesNotExist:
            messages.info(request,"User Profile is Here Please Fill Other Forms")
            return render(request,'dashboard_unuser.html',{'user':uname})
        except resume.DoesNotExist:
            messages.info(request,"User Profile & About is Here Please Fill Other Forms")
            return render(request,'dashboard_unuser.html',{'user':uname})
        except intrest.DoesNotExist:
            messages.info(request,"User Profile,About & Resume is Here Please Fill Other Forms")
            return render(request,'dashboard_unuser.html',{'user':uname})
        except testimonial.DoesNotExist:
            messages.info(request,"Please Add Client Testimonials , Your Services & Portfolio Images")
            return render(request,'dashboard_unuser.html',{'user':uname})
        except Service.DoesNotExist:
            messages.info(request,"Please Add Services & Portfolio Image")
            return render(request,'dashboard_unuser.html',{'user':uname})
        except Images.DoesNotExist:
            messages.info(request,"Please Add Portfolio Image")
            return render(request,'dashboard_unuser.html',{'user':uname})
    else :
        if request.method == "POST":
            if request.POST.get('Puname'):
                username = request.POST.get('Puname')
                uname = username
                print(uname)
                Pname = request.POST.get('Pname')
                Ppassion = request.POST.get('Ppassion')
                Pfacebook = request.POST.get('Pfacebook')
                Pinstagram = request.POST.get('Pinstagram')
                Ptwitter = request.POST.get('Ptwitter')
                Plikndin = request.POST.get('Plinkedin')
                Pskype = request.POST.get('Pskype')
                Profile = user_profile(user_name=uname,name=Pname,passion=Ppassion,
                facebook=Pfacebook,instagram=Pinstagram,linkidin=Plikndin,twitter=Ptwitter,skype=Pskype)
                Profile.save()
                messages.info(request,"User Profile is Saved Please Fill Other Forms")
                return render(request,'dashboard_unuser.html',{'user':uname})
            elif request.POST.get('Auname'):
                username = request.POST.get('Auname')
                uname=username
                Ajobprofile = request.POST.get('Ajobprofile')
                Ajobdesc = request.POST.get('Ajobdesc')
                Aphone = request.POST.get('Aphone')
                ADob = request.POST.get('Adob')
                Aage = request.POST.get('Aage')
                Adegree = request.POST.get('Adegree')
                if Adegree == "Higher Education":
                    s=0
                elif Adegree == "Bachelor":
                    s=1
                elif Adegree == "Diploma":
                    s=2
                elif Adegree == "Master":
                    s=2
                else :
                    s=0
                Afree = request.POST.get('Afree')
                if Afree == "Available":
                    v=0
                elif Afree == "Not-Available":
                    v=1
                else :
                    v=0
                Aemail = request.POST.get('Aemail')
                Acity = request.POST.get('Acity')
                Awebsite = request.POST.get('Awebsite')
                Aabout = request.POST.get('Aabout')
                Aclient = request.POST.get('Aclient')
                Aproject = request.POST.get('Aproject')
                Ahrs = request.POST.get('Ahrs')
                Aawards = request.POST.get('Aawards')
                About = user_about.objects.create(user=user_profile.objects.get(user_name=uname),job_profile=Ajobprofile,job_desc=Ajobdesc,Dob=ADob,
                age=Aage,website=Awebsite,degree=user_about.d_choice[s][1],Freelancer=user_about.f_choice[v][1],phone=Aphone,email=Aemail,city=Acity,about=Aabout,
                clients=Aclient,project=Aproject,Hrs=Ahrs,Awards=Aawards)
                About.save()
                messages.info(request,"User About is Saved Please Fill Other Forms")
                return render(request,'dashboard_unuser.html',{'user':uname})
            elif request.POST.get('Runame'):
                print("Resume")
                username = request.POST.get('Runame')
                uname = username
                print(uname)
                Rskill = request.POST.get('Rskills')
                Rper = request.POST.get('Rper')
                Rprimaryedutitle = request.POST.get('Rprimaryedutitle')
                Rprimaryeduname = request.POST.get('Rprimaryeduname')
                Rprimaryeduyrs = request.POST.get('Rprimaryeduyrs')
                Rprimaryedudesc = request.POST.get('Rprimaryeduyrs')
                Rsecedutitle = request.POST.get('Rsecedutitle')
                Rseceduname = request.POST.get('Rseceduname')
                Rseceduyrs = request.POST.get('Rseceduyrs')
                Rsecedudesc = request.POST.get('Rsecedudesc')
                Rprimaryjobtitle = request.POST.get('Rprimaryjobtitle')
                Rprimaryjobname = request.POST.get('Rprimaryjobname')
                Rprimaryjobyrs = request.POST.get('Rprimaryjobyrs')
                Rprimaryjobdesc = request.POST.get('Rprimaryjobdesc')
                Rsecjobtitle = request.POST.get('Rsecjobtitle')
                Rsecjobname = request.POST.get('Rsecjobname')
                Rsecjobyrs = request.POST.get('Rsecjobyrs')
                Rsecjobdesc = request.POST.get('Rsecjobdesc')
                Resume = resume.objects.create(user=user_profile.objects.get(user_name=uname),skill=Rskill,skillpercentage=Rper,highereducationtitle=Rprimaryedutitle,
                highereducationYear=Rprimaryeduyrs,highereducationName=Rprimaryeduname,highereducationDescription=Rprimaryedudesc,
                primaryeducationtitle=Rsecedutitle,primaryeducationYear=Rseceduyrs,primaryeducationName=Rseceduname,primaryeducationDescription=Rsecedudesc,
                primaryWorktitle=Rprimaryjobtitle,primaryWorkYear=Rprimaryjobyrs,primaryWorkName=Rprimaryjobname,primaryWorkDescription=Rprimaryjobdesc,
                secondaryWorktitle=Rsecjobtitle,secondaryWorkYear=Rsecjobyrs,secondaryWorkName=Rsecjobname,secondaryWorkDescription=Rsecjobdesc)
                Resume.save()
                messages.info(request,"User Resume is Saved Please Fill Other Forms")
                return render(request,'dashboard_unuser.html',{'user':uname})
            elif request.POST.get('Suname'):
                username = request.POST.get('Suname')
                uname=username
                print(uname)
                Sname = request.POST.get('Sname')
                Sicon = request.POST.get('Sicon')
                Sdesc = request.POST.get('Sdesc')
                Ser = Service.objects.create(user=user_profile.objects.get(user_name=uname),ServiceIcon=Sicon,ServiceName=Sname,ServiceDiscription=Sdesc)
                Ser.save()
                #messages.info(request,"User Service is Saved Please Fill Other Forms")
                messages.info(request,"Your Service is Saved")
                url = '/dashboard/?uname={}'.format(uname)
                return HttpResponseRedirect(url)
            elif request.POST.get('Iuname'):
                username = request.POST.get('Iuname')
                uname = username
                Iname = request.POST.get('Iname')
                Iicon = request.POST.get('Iicon')
                Inter = intrest.objects.create(user=user_profile.objects.get(user_name=uname),icon=Iicon,intrest=Iname)
                Inter.save()
                messages.info(request,"Your Intrest is Saved")
                url = '/dashboard/?uname={}'.format(uname)
                return HttpResponseRedirect(url)
            elif request.POST.get('Tuname'):
                username = request.POST.get('Tuname')
                uname = username
                Tname = request.POST.get('Tname')
                Tprofile = request.POST.get('Tprofile')
                Tword = request.POST.get('Tword')
                Timage = request.FILES.get('Timage')
                #print(Timage)
                Test = testimonial.objects.create(user=user_profile.objects.get(user_name=uname),ClientName=Tname,ClientProfile=Tprofile,ClientWords=Tword,
                ClientImage=Timage)
                Test.save()
                messages.info(request,"Client Testimonial is Saved")
                url = '/dashboard/?uname={}'.format(uname)
                return HttpResponseRedirect(url)
            elif request.POST.get('Imuname'):
                username = request.POST.get('Imuname')
                uname = username
                Imname = request.POST.get('Imname')
                Imcategory = request.POST.get('Imcategory')
                Imimage = request.FILES.get('Imimage')
                Img = Images.objects.create(User=user_profile.objects.get(user_name=uname),Name=Imname,Category=Imcategory,Image=Imimage)
                Img.save()
                messages.info(request,"Your Image is Saved")
                url = '/dashboard/?uname={}'.format(uname)
                return HttpResponseRedirect(url)
            else :
                return render(request,'dashboard_unuser.html',{'user':uname})
        return render(request,'dashboard_unuser.html',{'user':uname})

def main(request):
    if request.method == "GET":
        uname=request.GET.get('uname')
        print(uname)
    User = user_profile.objects.get(user_name=uname)
    User_abt = user_about.objects.get(user=uname)
    User_res = resume.objects.get(user=uname)
    Intrest = intrest.objects.filter(user=uname)
    Intrest = Intrest.order_by('intrest')
    Testimonial = testimonial.objects.filter(user=uname)
    Testimonial = Testimonial.order_by('ClientName')
    Services = Service.objects.filter(user=uname)
    Services = Services.order_by('ServiceName')
    Image = Images.objects.filter(User=uname)
    UEmail = User_abt.email
    skills = User_res.skill
    skills = skills.split(",")
    var1 = skills
    skillsper = User_res.skillpercentage
    skillsper = skillsper.split(",")
    List = []
    for i in Image:
        List.append(i.Category)
    List.sort()
    cat = set(List)
    cat = sorted(cat)
    print(cat)
    class main :
        def __init__(self,skills,skillsper) -> None:
            self.skills = skills
            self.per = skillsper
            self.num1 = 0
            self.num2 = 0
        def __iter__(self):
            return self
        def __postnext__(self):
            if self.num2 < len(skills):
                self.per = self.per[self.num2]
                self.num2 = self.num2+1
                return self.per
            else:
                StopIteration
        def __next__(self):
            if self.num1 < len(skills):
                skill = self.skills[self.num1]
                self.num1 = self.num1+1
                return skill
            else :
                raise StopIteration
            
    cls = main(skills,skillsper)
    itr = iter(cls)
    Dict = zip(var1,skillsper)
    if request.method == "POST":
        Name = request.POST.get('name')
        Email = request.POST.get('email')
        Subject = request.POST.get('subject')
        Message = request.POST.get('message')
        print(Name,Email,Subject,Message)
        '''send_mail(
            Subject , #subject
            Name + Message , #Body
            Email,#from Email
            [UEmail],#To Email
        )'''
        return render(request,'index.html',{'User':User,'Userabt':User_abt,
            'Userres':User_res,'Dict':Dict,'Intrest':Intrest,'Testimonial':Testimonial,
            'Services':Services,'Images':Image,'Category':cat,'Done':"sent-message"})
    else :
        return render(request,'index.html',{'User':User,'Userabt':User_abt,
            'Userres':User_res,'Dict':Dict,'Intrest':Intrest,'Testimonial':Testimonial,
            'Services':Services,'Images':Image,'Category':cat,'Done':""})
def testdel(request):
    user = request.GET.get('uname')
    user = user.split(" ")
    UserName = user[0]
    uname = UserName
    Name = user[2]
    Id = user[1]
    n=len(Id)
    Id = int(Id[3:n])
    Test = testimonial.objects.filter(id=Id).delete()
    messages.info(request,"Your Testimonial "+Name+" has been deleted")
    url = '/dashboard/?uname={}'.format(uname)
    return HttpResponseRedirect(url)
def imgdel(request):
    user = request.GET.get('uname')
    user = user.split(" ")
    UserName = user[0]
    uname = UserName
    Name = user[2]
    Id = user[1]
    n=len(Id)
    Id = int(Id[3:n])
    Test = Images.objects.filter(id=Id).delete()
    messages.info(request,"Your Image "+Name+" has been deleted")
    url = '/dashboard/?uname={}'.format(uname)
    return HttpResponseRedirect(url)
def servicedel(request):
    user = request.GET.get('uname')
    user = user.split(" ")
    UserName = user[0]
    uname = UserName
    Name = user[2]
    Id = user[1]
    n=len(Id)
    print(Id)
    Id = int(Id[3:n])
    Test = Service.objects.filter(id=Id).delete()
    messages.info(request,"Your Service "+Name+" has been deleted")
    url = '/dashboard/?uname={}'.format(uname)
    return HttpResponseRedirect(url)
def intrestdel(request):
    user = request.GET.get('uname')
    user = user.split(" ")
    UserName = user[0]
    uname = UserName
    Name = user[2]
    Id = user[1]
    n=len(Id)
    Id = int(Id[3:n])
    Test = intrest.objects.filter(id=Id).delete()
    messages.info(request,"Your Intrest "+Name+" has been deleted")
    url = '/dashboard/?uname={}'.format(uname)
    return HttpResponseRedirect(url)
def serviceupdate(request):
    if request.method == 'POST':
        Sname = request.POST.get('Sname')
        Sicon = request.POST.get('Sicon')
        Sdesc = request.POST.get('Sdesc')
        user = request.GET.get('uname')
        user = user.split(" ")
        UserName = user[0]
        uname = UserName
        Id = user[1]
        n=len(Id)
        Id = int(Id[3:n])
        Ser = Service.objects.filter(id=Id).update(ServiceIcon=Sicon,ServiceName=Sname,ServiceDiscription=Sdesc) 
        messages.info(request,"Your Services has been Update")
        url = '/dashboard/?uname={}'.format(uname)
        return HttpResponseRedirect(url)
    user = request.GET.get('uname')
    user = user.split(" ")
    UserName = user[0]
    uname = UserName
    Id = user[1]
    n=len(Id)
    Id = int(Id[3:n])
    Ser = Service.objects.get(id=Id)
    return render(request,'serviceupdate.html',{'Ser':Ser})
def intrestupdate(request):
    if request.method == 'POST':
        Iname = request.POST.get('Iname')
        Iicon = request.POST.get('Iicon')
        user = request.GET.get('uname')
        user = user.split(" ")
        UserName = user[0]
        uname = UserName
        Id = user[1]
        n=len(Id)
        Id = int(Id[3:n])
        Int = intrest.objects.filter(id=Id).update(icon=Iicon,intrest=Iname)
        messages.info(request,"Your Intrest has been Update")
        url = '/dashboard/?uname={}'.format(uname)
        return HttpResponseRedirect(url)
    user = request.GET.get('uname')
    user = user.split(" ")
    UserName = user[0]
    uname = UserName
    Id = user[1]
    n=len(Id)
    Id = int(Id[3:n])
    Int = intrest.objects.get(id=Id)
    return render(request,'intrestupdate.html',{'Int':Int})
def testupdate(request):
    if request.method == 'POST':
        Tname = request.POST.get('Tname')
        Tprofile = request.POST.get('Tprofile')
        Twords = request.POST.get('Twords')
        Timages = request.FILES.get('Timage')
        user = request.GET.get('uname')
        user = user.split(" ")
        UserName = user[0]
        uname = UserName
        Id = user[1]
        n=len(Id)
        Id = int(Id[3:n])
        Test = testimonial.objects.get(id=Id)
        Test.ClientName=Tname
        Test.ClientProfile=Tprofile
        Test.ClientWords=Twords
        Test.ClientImage=Timages
        Test.save()
        messages.info(request,"Your Testimonial has been Update")
        url = '/dashboard/?uname={}'.format(uname)
        return HttpResponseRedirect(url)
    user = request.GET.get('uname')
    user = user.split(" ")
    UserName = user[0]
    uname = UserName
    Id = user[1]
    n=len(Id)
    Id = int(Id[3:n])
    Test = testimonial.objects.get(id=Id)
    return render(request,'testimonialupdate.html',{'test':Test})
def imgupdate(request):
    if request.method == 'POST':
        Imname = request.POST.get('Imname')
        Imcat = request.POST.get('Imcategory')
        Imimg = request.FILES.get('Imimag')
        user = request.GET.get('uname')
        user = user.split(" ")
        UserName = user[0]
        uname = UserName
        Id = user[1]
        n=len(Id)
        Id = int(Id[3:n])
        Port2 = Images.objects.get(id=Id)
        Port2.Name = Imname
        Port2.Category = Imcat
        Port2.Image = Imimg
        Port2.save()
        messages.info(request,"Your Image has been Update")
        url = '/dashboard/?uname={}'.format(uname)
        return HttpResponseRedirect(url)
    user = request.GET.get('uname')
    user = user.split(" ")
    UserName = user[0]
    uname = UserName
    Id = user[1]
    n=len(Id)
    Id = int(Id[3:n])
    Port = Images.objects.get(id=Id)
    return render(request,'portfolioupdate.html',{'port':Port})
def profileupdate(request):
    if request.method == 'POST':
        Pname = request.POST.get('Pname')
        Ppassion = request.POST.get('Ppassion')
        Pfacebook = request.POST.get('Pfacebook')
        Pinstagram = request.POST.get('Pinstagram')
        Ptwitter = request.POST.get('Ptwitter')
        Plikndin = request.POST.get('Plinkedin')
        Pskype = request.POST.get('Pskype')
        user = request.GET.get('uname')
        uname = user
        Profile = user_profile.objects.filter(user_name=user).update(name=Pname,passion=Ppassion,facebook=Pfacebook,instagram=Pinstagram,linkidin=Plikndin,twitter=Ptwitter,skype=Pskype)
        messages.info(request,"Your Profile has been Update")
        url = '/dashboard/?uname={}'.format(uname)
        return HttpResponseRedirect(url)
    user = request.GET.get('uname')
    uname = user
    Profile = user_profile.objects.get(user_name=user)
    return render(request,'profileupdate.html',{'profile':Profile})
def aboutupdate(request):
    if request.method == 'POST':
        Ajobprofile = request.POST.get('Ajobprofile')
        Ajobdesc = request.POST.get('Ajobdesc')
        Aphone = request.POST.get('Aphone')
        ADob = request.POST.get('Adob')
        Aage = request.POST.get('Aage')
        Adegree = request.POST.get('Adegree')
        if Adegree == "Higher Education":
            s=0
        elif Adegree == "Bachelor":
            s=1
        elif Adegree == "Diploma":
            s=2
        elif Adegree == "Master":
            s=2
        else :
            s=0
        Afree = request.POST.get('Afree')
        if Afree == "Available":
            v=0
        elif Afree == "Not-Available":
            v=1
        else :
            v=0
        Aemail = request.POST.get('Aemail')
        Acity = request.POST.get('Acity')
        Awebsite = request.POST.get('Awebsite')
        Aabout = request.POST.get('Aabout')
        Aclient = request.POST.get('Aclient')
        Aproject = request.POST.get('Aproject')
        Ahrs = request.POST.get('Ahrs')
        Aawards = request.POST.get('Aawards')
        user = request.GET.get('uname')
        uname = user
        About=user_about.objects.get(user=uname)
        About.job_profile=Ajobprofile
        About.job_desc=Ajobdesc
        About.Dob=ADob
        About.age=Aage
        About.website=Awebsite
        About.degree=user_about.d_choice[s][1]
        About.Freelancer=user_about.f_choice[v][1]
        About.phone=Aphone
        About.email=Aemail
        About.city=Acity
        About.about=Aabout
        About.clients=Aclient
        About.project=Aproject
        About.Hrs=Ahrs
        About.Awards=Aawards
        messages.info(request,"Your About has been Update")
        url = '/dashboard/?uname={}'.format(uname)
        return HttpResponseRedirect(url)
    user = request.GET.get('uname')
    uname = user
    About = user_about.objects.get(user=uname)
    return render(request,'aboutupdate.html',{'about':About})
def resumeupdate(request):
    if request.method == 'POST':
        Rskill = request.POST.get('Rskills')
        Rper = request.POST.get('Rper')
        Rprimaryedutitle = request.POST.get('Rprimaryedutitle')
        Rprimaryeduname = request.POST.get('Rprimaryeduname')
        Rprimaryeduyrs = request.POST.get('Rprimaryeduyrs')
        Rprimaryedudesc = request.POST.get('Rprimaryeduyrs')
        Rsecedutitle = request.POST.get('Rsecedutitle')
        Rseceduname = request.POST.get('Rseceduname')
        Rseceduyrs = request.POST.get('Rseceduyrs')
        Rsecedudesc = request.POST.get('Rsecedudesc')
        Rprimaryjobtitle = request.POST.get('Rprimaryjobtitle')
        Rprimaryjobname = request.POST.get('Rprimaryjobname')
        Rprimaryjobyrs = request.POST.get('Rprimaryjobyrs')
        Rprimaryjobdesc = request.POST.get('Rprimaryjobdesc')
        Rsecjobtitle = request.POST.get('Rsecjobtitle')
        Rsecjobname = request.POST.get('Rsecjobname')
        Rsecjobyrs = request.POST.get('Rsecjobyrs')
        Rsecjobdesc = request.POST.get('Rsecjobdesc')
        user = request.GET.get('uname')
        uname = user
        Resume = resume.objects.filter(user=uname).update(skill=Rskill,skillpercentage=Rper,highereducationtitle=Rprimaryedutitle,
                highereducationYear=Rprimaryeduyrs,highereducationName=Rprimaryeduname,highereducationDescription=Rprimaryedudesc,
                primaryeducationtitle=Rsecedutitle,primaryeducationYear=Rseceduyrs,primaryeducationName=Rseceduname,primaryeducationDescription=Rsecedudesc,
                primaryWorktitle=Rprimaryjobtitle,primaryWorkYear=Rprimaryjobyrs,primaryWorkName=Rprimaryjobname,primaryWorkDescription=Rprimaryjobdesc,
                secondaryWorktitle=Rsecjobtitle,secondaryWorkYear=Rsecjobyrs,secondaryWorkName=Rsecjobname,secondaryWorkDescription=Rsecjobdesc)
        messages.info(request,"Your Profile has been Update")
        url = '/dashboard/?uname={}'.format(uname)
        return HttpResponseRedirect(url)
    user = request.GET.get('uname')
    uname = user
    Resume = resume.objects.get(user=uname)
    return render(request,'resumeupdate.html',{'Res':Resume})
def userupdate(request):
    return HttpResponse(request,"You can update your user info here") 
def changepass(request):
    return HttpResponse(request,"You can change your password info here")
def userinfo(request):
    return HttpResponse(request,"You can see your user info here")