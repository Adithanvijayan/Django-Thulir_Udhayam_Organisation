from django.shortcuts import render,redirect
from .models import Members,Support,Opinion,Contact
from django.http import HttpResponseRedirect

def index(request):
    joinFlag = -1
    supportCount = Support.objects.all().count()
    if request.method == "POST":
        email = request.POST['email']
        try:
            supportObj1 = Support.objects.create(email=email)
            supportCount = Support.objects.all().count()
            joinFlag = 0
        except:
            joinFlag = 1
        return render(request,'index.html',{"joinFlag":joinFlag, "supportCount":supportCount, "successMsg":"Thank You For Your Support"})
    return render(request,'index.html',{"supportCount":supportCount,"joinFlag":joinFlag})

def joinForm(request):
    joinFlag = -1
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        number = request.POST['number']
        pin = request.POST['pin']
        try:
            membersObj = Members.objects.create(email=email, name=name, number=number, pin=pin)
            joinFlag = 0
        except:
            joinFlag = 1
        urlName = request.META['HTTP_REFERER']
        urlName = urlName.split('/')
        fileName = urlName[-1]+".html"
        print(fileName)
        # return redirect(request.META['HTTP_REFERER'])
        return render(request,fileName,{"joinFlag":joinFlag, "successMsg":"Joined Successfully"})
    return render(request,'index.html',{"joinFlag":joinFlag})

def opinion(request):
    joinFlag = -1
    if request.method == "POST":
        p_id = request.POST['id']
        opinion = request.POST['opinion']
        try:
            supportObj1 = Opinion.objects.create(p_id=p_id, opinion=opinion)
            joinFlag = 0
        except:
            joinFlag = 1
        return render(request,'opinion.html',{"joinFlag":joinFlag, "successMsg":"Submitted Successfully"})
    return render(request,'opinion.html',{"joinFlag":joinFlag})

def agenda(request):
    joinFlag = -1
    return render(request,'agenda.html',{"joinFlag":joinFlag})

def happening(request):
    joinFlag = -1
    return render(request,'happening.html',{"joinFlag":joinFlag})

def blog(request):
    joinFlag = -1
    return render(request,'blog.html',{"joinFlag":joinFlag})

def contact(request):
    joinFlag = -1
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        number = request.POST['number']
        subject = request.POST['subject']
        message = request.POST['message']
        try:
            membersObj = Contact.objects.create(name=name, email=email, number=number, subject=subject, message=message)
            joinFlag = 0
        except:
            joinFlag = 1
        return render(request,'contact.html',{"joinFlag":joinFlag, "successMsg":"We will get back to you shortly"})
    return render(request,'contact.html',{"joinFlag":joinFlag})
