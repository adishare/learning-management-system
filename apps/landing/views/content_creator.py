from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from academy.models.content_creator import ContentCreator
from academy.forms.content_creator import ContentCreatorForm
from django.template import RequestContext
from academy.models.academy import Academy

@login_required
def index(request):
    request.user.set_active_role('content_creator')
    content_creator_list = ContentCreator.objects.all()
    return render(request, "landing/content_creator/index.html", locals())

@login_required
def add(request):
    form = ContentCreatorForm()
    academy_list = Academy.objects.all()
    if request.method == "POST":
        data = request.POST.copy()
        form = ContentCreatorForm(data)
        if form.is_valid():
            form.save()
            request.method = 'GET'
            return index(request)
    return render(request, 'academy/content_creator/add.html', locals())

@login_required
def edit(request, id):
    content_creator = ContentCreator.objects.get(id=id)
    form = ContentCreatorForm(instance=content_creator)
    if request.method == "POST":
        data = request.POST
        form = ContentCreatorForm(data, instance=content_creator)
        if form.is_valid():
            form.save()
            request.method = 'GET'
            return index(request)
    return render(request, 'academy/content_creator/edit.html', locals())

@login_required
def delete(request, id):
    ContentCreator.objects.filter(id=id).delete()
    return index(request)