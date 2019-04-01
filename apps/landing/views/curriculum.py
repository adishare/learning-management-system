from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from competency.models.curriculum import Curriculum
from competency.forms.curriculum import CurriculumForm
from competency.models.curriculum import Curriculum

@login_required
def index(request):
    request.user.set_active_role('curriculum')
    curriculum_list = Curriculum.objects.all()
    return render(request, "landing/curriculum/index.html", locals())
