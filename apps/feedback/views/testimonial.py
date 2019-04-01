from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from feedback.models.feedback import Testimonial, TestimonialAnswer, TestimonialCategory
from feedback.forms.testimonial import TestimonialForm
from academy.models.event import Event


@login_required
def index(request):
    testimonial_list = Testimonial.objects.all()
    event_list = Event.objects.all()
    return render(request, 'feedback/testimonial/index.html', locals())

@login_required
def view(request):
    # article = Article.objects.get(slug=slug)
    category_list = TestimonialCategory.objects.all()
    testimonial_list = Testimonial.objects.all()
    return render(request, 'feedback/testimonial/view.html', locals())

@login_required
def add(request):
    category_list = TestimonialCategory.objects.all()
    testimonial_list = Testimonial.objects.all()

    # testimonial_category = testimonial_list.objects.filter(category=category_list)
    
    form = TestimonialForm()
    if request.method == "POST":
        data = request.POST.copy()
        form = TestimonialForm(data)
        if form.is_valid():
            form.save()
            return redirect('feedback-testimonial-index')
    return render(request, 'feedback/testimonial/add.html', locals())