from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from content.forms.quiz import QuizQuestionForm
from content.models.quiz import QuizQuestion

@login_required
def index(request):
    quiz_question_list = QuizQuestion.objects.all()
    return render(request, 'content/quiz/index.html', locals())

@login_required
def view(request, id):
    quiz_question = QuizQuestion.objects.get(id=id)
    return render(request, 'content/quiz/view.html', locals())

@login_required
def add(request):
    form = QuizQuestionForm()
    if request.method == "POST":
        data = request.POST
        form = QuizQuestionForm(data)
        if form.is_valid():
            question = form.save()
            return redirect('content-quiz-view', id=question.id)
        else:
            messages.error(request, "Form can't be saved")
    return render(request, 'content/quiz/add.html', locals())

@login_required
def edit(request, id):
    quiz_question = QuizQuestion.objects.get(id=id)
    form = QuizQuestionForm(instance=quiz_question)
    if request.method == "POST":
        data = request.POST
        form = QuizQuestionForm(data, instance=quiz_question)
        if form.is_valid():
            form.save()
            messages.success(request, "Content saved successfuly")
            return redirect('content-quiz-view', id=id)
        else:
            messages.error(request, "Form can't be saved")
    return render(request, 'content/quiz/edit.html', locals())

