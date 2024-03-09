from mailbox import Message

from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Register, Packages
from .models import VibePackages  # Import the VibePackages model

def checkvibelogin(request):
    if request.method == "POST":
        name = request.POST["uname"]
        pwd = request.POST["pwd"]
        flag = Register.objects.filter(username=name, password=pwd).exists()

        if flag:  # flag is not empty
            if name == "rosh":  # roshini is admin
                messages.info(request, "This is admin  page")
                return render(request, "adminhome.html")
            else:
                messages.info(request, "This is User's  page")
                return render(request, "musichome.html")
        else:
            messages.info(request, "Your credentials are not correct")
            return render(request, "loginfail.html")

def checkRegistration(request):

    if request.method == "POST":
        name = request.POST["name"]
        addr = request.POST["addr"]
        email = request.POST["email"]
        phno = request.POST["phno"]
        uname = request.POST["uname"]
        pwd = request.POST["pwd"]
        cpwd = request.POST["cpwd"]
        if pwd == cpwd:
            if Register.objects.filter(username=uname).exists():
                messages.info(request , "username existing...")
                return render(request,"register.html")
            elif Register.objects.filter(email=email).exists():
                messages .info(request, "email existing...")
                return render(request, "register.html")
            else:
                user = Register.objects.create(name=name,address=addr,email=email,phno=phno,username=uname,password=pwd)
                user.save()
                messages.info(request ," usercreated...")
                return render(request, "login.html")
        else:
            messages.info(request, "password is not matching...")
            return render(request, "register.html")

def checkpackages(request):
    if request.method == "POST":
        musiccode = request.POST.get("musiccode")
        musictitle = request.POST.get("musictitle")
        musicpackage = request.POST.get("musicpackage")
        musicdescription = request.POST.get("musicdesc")

        if musiccode and musictitle and musicpackage and musicdescription:
            pack = Packages.objects.create(musiccode=musiccode, musictitle=musictitle, musicpackage=musicpackage,
                                           musicdesc=musicdescription)
            pack.save()
            messages.info(request, "Data inserted successfully")
        else:
            messages.error(request, "Please fill in all the fields")

    return render(request, "package.html")



def viewplaces(request):
    data = VibePackages.objects.all()  # Retrieve all instances of VibePackages
    return render(request, "viewplaces.html", {"placesdata": data})

def checkChangePassword(request):
    if request.method=="POST":
        uname=request.POST["uname"]
        opwd=request.POST["opwd"]
        npwd=request.POST["npwd"]
        flag=Register.objects.filter(username=uname,password=opwd).values()
        if flag:
            Register.objects.filter(username=uname,password=opwd).update(password=npwd)
            return render(request,"index.html")
        else:
            messages.info(request,"Password Updated")
            return render(request, "index.html")
    else:
            return render(request,"changepassword.html")

def logout(request):
    messages.info(request,"Logout")
    return render(request,"index.html")



def contactmail(request):
    if request.method == "POST":
        subject = request.POST['subject']
        message = request.POST['message']
        send_mail(subject,message,'lukkaroshini@gmail.com',['lukkaroshini@gmail.com'],fail_silently=False)
        return HttpResponse("Mailsent Successfully")

    else:
        return render(request,'mail.html')


