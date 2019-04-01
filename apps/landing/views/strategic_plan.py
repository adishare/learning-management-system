from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from academy.models.strategic_plan import StrategicPlan, StrategicPlanField
from academy.forms.strategic_plan import StrategicPlanForm
from django.template import RequestContext
from academy.models.academy import Academy

@login_required
def index(request):
    request.user.set_active_role('strategic_plan')  
    strategic_list = StrategicPlan.objects.all()
    fields = StrategicPlanField.objects.exclude(name="Strategic Initiative")
    return render(request, "landing/strategic_plan/index.html", locals())

@login_required
def add(request):
    form = StrategicPlanForm()
    if request.method == "POST":
        data = request.POST.copy()
        form = StrategicPlanForm(data)
        if form.is_valid():
            form.save()
            return redirect('landing-strategic-plan-index')
    return render(request, 'academy/strategic_plan/add.html', locals())

@login_required
def edit(request, id):
    strategic_plan = StrategicPlan.objects.get(id=id)   
    form = StrategicPlanForm(instance=strategic_plan)
    if request.method == "POST":
        data = request.POST.copy()
        form = StrategicPlanForm(data, instance=strategic_plan)
        if form.is_valid():
            form.save()
            return redirect('landing-strategic-plan-index')
    return render(request, 'academy/strategic_plan/edit.html', locals())

@login_required
def delete(request, id):
    StrategicPlan.objects.filter(id=id).delete()
    return index(request)
