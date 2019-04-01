from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from academy.models.event import Event
from academy.forms.event import EventForm
from academy.models.academy import Academy

@login_required
def add(request):
    form = EventForm()
    if request.method == "POST":
        data = request.POST.copy()
        form = EventForm(data)
        if form.is_valid():
            # new_form = form.save(commit=False)
            # new_form.author = request.user
            form.save()
            return redirect('landing-event-manager-index')
    return render(request, 'academy/event/add.html', locals())

@login_required
def edit(request,id):
    event_manager = Event.objects.get(id=id)
    form = EventForm(instance=event_manager)
    if request.method == "POST":
        data = request.POST.copy()
        form = EventForm(data, instance=event_manager)
        if form.is_valid():
            # new_form = form.save(commit=False)
            # new_form.author = request.user
            form.save()
            event_manager_list = Event.objects.all()
            return render(request, "landing/event_manager/index.html", locals())
    return render(request, 'academy/event/edit.html', locals())    

@login_required
def delete(request, id):
    Event.objects.filter(id=id).delete()
    return redirect("landing-event-manager-index")

@login_required
def set_on_going(request, id):
    event = Event.objects.get(id=id)
    event.set_on_going(request.user)
    return redirect("landing-event-manager-index")

@login_required
def set_finish(request, id):
    event = Event.objects.get(id=id)
    event.set_finish(request.user)
    return redirect("landing-event-manager-index")
