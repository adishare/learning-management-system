from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from competency.models.curriculum import Curriculum
from competency.forms.curriculum import CurriculumForm
from landing.views.curriculum import index
from academy.models.learning_activity import LearningActivity
from django.forms import ModelForm

class addLearningActivityForm(ModelForm):
    class Meta:
        model = Curriculum
        fields = ['learning_activity']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        

@login_required
def add(request):
    cycle_list = LearningActivity.objects.all()
    form = CurriculumForm()
    if request.method == "POST":
        data = request.POST.copy()
        form = CurriculumForm(data)
        if form.is_valid():
            cur = form.save()
            return redirect('competency-curriculum-view', id=cur.id)
    return render(request, 'competency/curriculum/add.html', locals())

@login_required
def view(request, id):
    curriculum = Curriculum.objects.get(id=id)
    add_learning_activity_form = addLearningActivityForm(instance=curriculum)
    add_learning_activity_form.fields["learning_activity"].queryset = LearningActivity.objects.exclude(id__in=curriculum.learning_activity.all())
    return render(request, 'competency/curriculum/view.html', locals())

@login_required
def add_learning_activity(request, id):
    curriculum = Curriculum.objects.get(id=id)
    add_learning_activity_form = addLearningActivityForm(instance=curriculum)
    if request.method == "POST":
        new_learning_activity_list = request.POST.getlist('learning_activity')
        curriculum.learning_activity.add(*new_learning_activity_list)
        return redirect('competency-curriculum-view', id=id)

@login_required
def remove_learning_activity(request, id, learningActivityId):
    curriculum = Curriculum.objects.get(id=id)
    learning_activity = LearningActivity.objects.get(id=learningActivityId)
    curriculum.learning_activity.remove(learning_activity)
    return redirect('competency-curriculum-view', id=id)

@login_required
def edit(request,id):
    curriculum = Curriculum.objects.get(id=id)
    form = CurriculumForm(instance=curriculum)
    if request.method == "POST":
        data = request.POST.copy()
        form = CurriculumForm(data, instance=curriculum)
        if form.is_valid():
            # new_form = form.save(commit=False)
            # new_form.author = request.user
            form.save()
            return redirect('landing-curriculum-index')
    return render(request, 'competency/curriculum/edit.html', locals())    

@login_required
def delete(request, id):
    Curriculum.objects.filter(id=id).delete()
    return index(request)