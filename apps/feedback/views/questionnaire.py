from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from feedback.forms.questionnaire import QuestionnaireForm
from academy.models.event import Event
from human_resource.models.participant import Participant
from feedback.models.feedback import Questionnaire, QuestionnaireAnswer

@login_required
def index(request):
    questionnaire_list = Questionnaire.objects.all()
    event_list = Event.objects.all()
    return render(request, 'feedback/questionnaire/index.html', locals())

@login_required
def participant(request):
    participant_list = Participant.objects.all()
    return render(request, 'feedback/questionnaire/participant.html', locals())

@login_required
def add(request):
    question_list = Questionnaire.objects.all()
    form = QuestionnaireForm()
    if request.method == "POST":
        data = request.POST.copy()
        form = QuestionnaireForm(data)
        if form.is_valid():
            form.save()
            return redirect('feedback-questionnaire-participant-list')
    return render(request, 'feedback/questionnaire/add.html', locals())

