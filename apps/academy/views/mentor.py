from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from academy.models.participant_event import ParticipantEvent

@login_required
def view(request):
    request.user.set_active_role('mentor')
    mentor_list = ParticipantEvent.objects.all()
    return render(request, "academy/mentor/view.html", locals())