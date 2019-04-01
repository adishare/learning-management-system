from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from academy.models.participant_event import ParticipantEvent
from academy.forms.participant_event import ParticipantEventForm
from academy.models.academy import Academy

@login_required
def add(request):
    form = ParticipantEventForm()
    if request.method == "POST":
        data = request.POST.copy()
        form = ParticipantEventForm(data)
        if form.is_valid():
            # new_form = form.save(commit=False)
            # new_form.author = request.user
            form.save()
            return redirect('landing-participant-event-index')
    return render(request, 'academy/participant_event/add.html', locals())

@login_required
def edit(request,id):
    participant_event = ParticipantEvent.objects.get(id=id)
    form = ParticipantEventForm(instance=participant_event)
    if request.method == "POST":
        data = request.POST.copy()
        form = ParticipantEventForm(data, instance=participant_event)
        if form.is_valid():
            # new_form = form.save(commit=False)
            # new_form.author = request.user
            form.save()
           participant_event_list = ParticipantEvent.objects.all()
            return render(request, "landing/participant-event/index.html", locals())
    return render(request, 'academy/participant_event/edit.html', locals())    

@login_required
def delete(request, id):
    ParticipantEvent.objects.filter(id=id).delete()
    return redirect("landing-participant-event-index")

@login_required
def set_on_going(request, id):
    participant_event = ParticipantEvent.objects.get(id=id)
    participant_event.set_on_going(request.user)
    return redirect("landing-participant-event-index")

@login_required
def set_finish(request, id):
    participant_event = ParticipantEvent.objects.get(id=id)
    participant_event.set_finish(request.user)
    return redirect("landing-participant-event-index")
