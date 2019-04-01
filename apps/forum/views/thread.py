from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from forum.models.thread import Thread, Comment
from forum.forms.thread import ThreadForm

def index(request):
    thread_list = Thread.objects.all()
    return render(request, 'forum/thread/index.html', locals())

def view(request, id):
    thread = Thread.objects.get(id=id)
    return render(request, 'forum/thread/view.html', locals())

@login_required
def add_comment(request, id):
    thread = Thread.objects.get(id=id)
    if request.method == "POST":
        data = request.POST
        new_comment = Comment.objects.create(
            author = request.user,
            thread = thread,
            body = data['comment']
        )
        messages.success(request, "Comment posted successfuly")
        return redirect('forum-thread-view', id=id)
    return render(request, 'content/quiz/add.html', locals())

@login_required
def add(request):
    form = ThreadForm()
    if request.method == "POST":
        data = request.POST
        new_thread = Thread(
            title = data['title'],
            author = request.user,
            body = data['content'],
        )
        if len(data['forum']) > 0:
            new_thread.forum = Forum.objects.get(id=data['forum'])
        new_thread.save()
        messages.success(request, "Thread posted successfuly")
        return redirect('forum-thread-index')

    return render(request, 'forum/thread/add.html', locals())

@login_required
def edit(request, id):
    thread = Thread.objects.get(id=id)
    form = ThreadForm(instance=thread)
    if request.method == "POST":
        data = request.POST
        form = ThreadForm(data, instance=thread)
        if form.is_valid():
            thread = form.save()
            messages.success(request, "Thread edited successfuly")
            return redirect('forum-thread-view' , id=thread.id)
        else:
            print(form.errors)
    return render(request, 'forum/thread/edit.html', locals())

@login_required
def delete(request, id):
    thread = Thread.objects.get(id=id)
    thread.delete()
    return redirect('forum-thread-index')