from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from academy.models.learning_plan import LearningPlan
from academy.forms.learning_plan import LearningPlanForm

@login_required
def index(request):
    learning_plan_list = LearningPlan.objects.all()
    return render(request, "academy/learning_plan/index.html", locals())

@login_required
def add(request):
    form = LearningPlanForm()
    if request.method == "POST":
        data = request.POST
        form = LearningPlanForm(data)
        if form.is_valid():
            form.save()
            return redirect('academy-learning-plan-add')
    return render(request, 'academy/learning_plan/add.html', locals())

@login_required
def edit(request,id):
    learning_plan = LearningPlan.objects.get(id=id)
    form = LearningPlanForm(instance=learning_plan)
    if request.method == "POST":
        data = request.POST
        form = LearningPlanForm(data, instance=learning_plan)
        if form.is_valid():
            form.save()
            learning_plan_list = LearningPlan.objects.all()
            request.method == "GET"
            return redirect('academy-learning-plan-index')
    return render(request, 'academy/learning_plan/edit.html', locals())    

@login_required
def delete(request, id):
    LearningPlan.objects.filter(id=id).delete()
    return index(request)