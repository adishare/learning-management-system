from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from academy.models.participant_event import ParticipantEvent

@login_required
def index(request):
    request.user.set_active_role('mentor')
    mentor_list = ParticipantEvent.objects.all()
    return render(request, "landing/mentor/index.html", locals())

def count(View):
    count_state = ParticipantEvent.objects.filter(state='Hadir').count()
    return index(View)


@login_required
def delete(request, id):
    ParticipantEvent.objects.filter(id=id).delete()
    return index(request)