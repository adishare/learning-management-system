from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    if request.user.active_role and request.user.active_role.landing_url_name:    
        return redirect(request.user.active_role.landing_url_name)
    else:
        return redirect("landing-student-index")