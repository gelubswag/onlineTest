from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, decorators
from django.http import HttpResponseRedirect
def log(request):
    if request.user.is_authenticated:
        return redirect("testApp:main")
    err = "Ошибка авторизации"
    context = {
        "pageTitle" : "Авторизация"
    }
    if request.method == "GET":
        return render(request,"logauth/login.html", context)
    else:
        user = [request.POST["username"], request.POST["password"]]
        user = authenticate(request,username=user[0], password=user[1])
        if user:
            login(request, user)
            return redirect("testApp:main")
        else:
            context["err"] = err
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@decorators.login_required
def logaut(request):
    logout(request)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
# Create your views here.
