from django.shortcuts import render, redirect
from testApp.models import Subject
from testApp.forms import SubjectForm
from django.contrib.auth import decorators
# Create your views here.

def testpage(request):
    return render(request, "test.html")

def main(request):
    context = {
        "pageTitle" : "Дисциплины",
        "subjects" : Subject.objects.all().order_by("name")
    }
    return render(request, "test/main.html",context)

@decorators.login_required
def addSubject(request):
    if not(request.user.is_staff):
        return
    if request.method == "GET":
        context = {
            "pageTitle" : "Добавить дисциплину",
            "form" : SubjectForm()
        }
        return render(request, "test/subjectForm.html", context)
    else:
        try:
            subj = request.POST["name"]
            subj = Subject.objects.create(name=subj)
            return redirect("testApp:main")
        except Exception as err:
            context = {
                    "pageTitle" : "Добавить дисциплину",
                    "subjects" : Subject.objects.all().order_by("name"),
                    "err" : err,
                    "form" : SubjectForm()
                    }
            return render(request, "test/subjectForm.html", context)

@decorators.login_required
def deleteSubject(request, subId):
    if not(request.user.is_staff):
        return redirect("testApp:main")
    try:
        subj = Subject.objects.filter(id=subId).all()[0]
        subj.delete()
    except:
        pass
    
    return redirect("testApp:main")



@decorators.login_required
def detailsSubject(request,subId):
    subj = Subject.objects.filter(id=subId).all()[0]
    context = {
        "pageTitle" : subj.name,
    }
    return render(request, "test/subjectDetails.html",context)

@decorators.login_required
def changeSubject(request,subId):
    if not(request.user.is_staff):
        return redirect("testApp:main")
    if request.method=="GET":
        context = {
            "pageTitle" : "Изменить название",
            "form" : SubjectForm()
        }
        return render(request, "test/subjectForm.html", context)
    else:
        subj = Subject.objects.filter(id=subId).all()[0]
        subj.name = request.POST["name"]
        subj.save()
        return redirect("testApp:main")