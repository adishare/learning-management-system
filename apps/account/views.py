import sys
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth import logout, authenticate, login
from django.utils.translation import ugettext_lazy as _
from django.contrib import messages

def login_page(request):
    if request.user.is_authenticated :
        return redirect("landing-index")
    if request.method == "POST" :
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if not user.is_active :
                messages.error(request, _("User doesn't active, please contact administrator !"))
                return redirect("account-login")
            
            login(request, user)
            # messages.success(request, "Welcome %s" % user.full_name or user)
            if request.GET.get("next"):
                return redirect(request.GET.get("next"))
            else :
                return redirect("landing-index")
        else:
            messages.add_message(request, messages.ERROR, _('Credential invalid !'))
    return render(request, "login/index.html")

def logout_page(request):
    logout(request)
    # messages.success(request, _("Thank you, you signout succesfuly"))
    return redirect("landing-index")
