from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from academy.models.event import Event
from academy.models.academy import Academy

@login_required
def index(request):
    request.user.set_active_role('event_manager')
    event_manager_list = Event.objects.all()
    return render(request, "landing/event_manager/index.html", locals())