from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from academy.models.event_plan import EventPlan
from academy.forms.event_plan import EventPlanForm
from academy.models.academy import Academy

@login_required
def add(request):
    form = EventPlanForm()
    if request.method == "POST":
        data = request.POST.copy()
        form = EventPlanForm(data)
        if form.is_valid():
            # new_form = form.save(commit=False)
            # new_form.author = request.user
            form.save()
            return redirect('landing-event-plan-index')
    return render(request, 'academy/event_plan/add.html', locals())

@login_required
def edit(request,id):
    event_manager = EventPlan.objects.get(id=id)
    form = EventPlanForm(instance=event_manager)
    if request.method == "POST":
        data = request.POST.copy()
        form = EventPlanForm(data, instance=event_manager)
        if form.is_valid():
            # new_form = form.save(commit=False)
            # new_form.author = request.user
            form.save()
            event_plan_list = EventPlan.objects.all()
            return render(request, "landing/event_plan/index.html", locals())
    return render(request, 'academy/event_plan/edit.html', locals())    

@login_required
def delete(request, id):
    EventPlan.objects.filter(id=id).delete()
    return redirect("landing-event-plan-index")

# @login_required
# def set_on_going(request, id):
#     event = Event.objects.get(id=id)
#     event.set_on_going(request.user)
#     return redirect("landing-event-manager-index")

# @login_required
# def set_finish(request, id):
#     event = Event.objects.get(id=id)
#     event.set_finish(request.user)
#     return redirect("landing-event-manager-index")
