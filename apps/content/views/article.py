from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from content.forms.article import ArticleForm
from content.models.article import Article, ArticleCategory

@login_required
def index(request):
    article_list = Article.objects.filter(author=request.user)
    return render(request, 'content/article/index.html', locals())

@login_required
def view(request, slug):
    article = Article.objects.get(slug=slug)
    return render(request, 'content/article/view.html', locals())

@login_required
def add(request):
    form = ArticleForm()
    if request.method == "POST":
        data = request.POST
        form = ArticleForm(data)
        print(data)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.author = request.user
            new_form.save()
            form.save_m2m()
            messages.success(request, "Content saved successfuly")
            return redirect('content-article-edit', slug=new_form.slug)
        else:
            messages.error(request, "Form can't be saved")
    return render(request, 'content/article/add.html', locals())

@login_required
def edit(request, slug):
    article = Article.objects.get(slug=slug)
    form = ArticleForm(instance=article)
    if request.method == "POST":
        data = request.POST
        form = ArticleForm(data, request.FILES, instance=article)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.author = request.user
            new_form.save()
            form.save_m2m()
            messages.success(request, "Content saved successfuly")
            return redirect('content-article-edit', slug=new_form.slug)
        else:
            messages.error(request, "Form can't be saved")
    return render(request, 'content/article/edit.html', locals())
