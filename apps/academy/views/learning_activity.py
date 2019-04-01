from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from academy.models.learning_activity import LearningActivity
from academy.forms.learning_activity import LearningActivityForm
from attachment.models.attachment import Attachment
from competency.models.curriculum import Curriculum

@login_required
def index(request):
    learning_activity_list = LearningActivity.objects.all()
    attachment_list = Attachment.objects.all()
    return render(request, "academy/learning_activity/index.html", locals())

@login_required
def view(request, id):
    learning_activity = LearningActivity.objects.get(id=id)
    return render(request, "academy/learning_activity/view.html", locals())

@login_required
def add(request):
    form = LearningActivityForm()
    if request.method == "POST":
        data = request.POST
        form = LearningActivityForm(data)
        if form.is_valid():
            new_form = form.save()
            return redirect('academy-learning-activity-edit', id=new_form.id)
    return render(request, 'academy/learning_activity/add.html', locals())

@login_required
def edit(request,id):
    learning_activity = LearningActivity.objects.get(id=id)
    form = LearningActivityForm(instance=learning_activity)
    if request.method == "POST":
        data = request.POST
        form = LearningActivityForm(data, request.FILES, instance=learning_activity)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.save()
            form.save_m2m()
            learning_activity_list = LearningActivity.objects.all()
            request.method == "GET"
            return render(request, "academy/learning_activity/index.html", locals())
    return render(request, 'academy/learning_activity/edit.html', locals())    

@login_required
def delete(request, id):
    LearningActivity.objects.filter(id=id).delete()
    return index(request)