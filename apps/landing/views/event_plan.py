from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from academy.models.event_plan import EventPlan
from academy.models.academy import Academy

@login_required
def index(request):
    event_plan_list = EventPlan.objects.all()
    return render(request, "landing/event_plan/index.html", locals())