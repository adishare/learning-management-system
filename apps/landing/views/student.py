from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    request.user.set_active_role('student')
    return render(request, "landing/student/index.html")

