from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from forum.models.forum import Forum
from forum.models.thread import Thread
from forum.forms.thread import ThreadForm
from forum.forms.forum import ForumForm

def index(request):
    forum_list = Forum.objects.all()
    return render(request, 'forum/forum/index.html', locals())

def view(request, id):
    forum = Forum.objects.get(id=id)
    return render(request, 'forum/forum/view.html', locals())


@login_required
def add(request):
    form = ForumForm()
    if request.method == "POST":
        data = request.POST
        form = ForumForm(data)
        if form.is_valid():
            new_forum = form.save()
            messages.success(request, "Forum created successfuly")
            return redirect('forum-view' , id=new_forum.id)
        else:
            messages.success(request, "Error creating forum")
    return render(request, 'forum/forum/add.html', locals())

@login_required
def edit(request, id):
    forum = Forum.objects.get(id=id)
    form = ForumForm(instance=forum)
    if request.method == "POST":
        data = request.POST
        form = ForumForm(data, instance=forum)
        if form.is_valid():
            new_forum = form.save()
            messages.success(request, "Forum updated successfuly")
            return redirect('forum-view' , id=new_forum.id)
        else:
            messages.success(request, "Error updating forum")
    return render(request, 'forum/forum/edit.html', locals())


@login_required
def addthread(request, id):
    form = ThreadForm()
    forum = Forum.objects.get(id=id)
    if request.method == "POST":
        data = request.POST
        new_thread = Thread(
            title = data['title'],
            author = request.user,
            body = data['content'],
            forum = forum
        )
        new_thread.save()
        messages.success(request, "Thread posted successfuly")
        return redirect('forum-thread-view' ,id=new_thread.id)

    return render(request, 'forum/forum/addthread.html', locals())
