from django.contrib import admin
from .models.feedback import Testimonial, Questionnaire, QuestionnaireAnswer, TestimonialAnswer, TestimonialCategory, QuestionnaireCategory

class TestimonialAdmin(admin.ModelAdmin):
    menu_title = "Testimonial"
    menu_group = "Feedback"
    list_display = ['code', 'event', 'category' , 'question', 'concealed']

class QuestionnaireAdmin(admin.ModelAdmin):
    menu_title = "Quistionnaire"
    menu_group = "Feedback"
    list_display = ['code', 'event', 'category', 'question']

class QuestionnaireAnswerAdmin(admin.ModelAdmin):
    menu_title = "Questionnaire Answer"
    menu_group = "Feedback"
    list_display = ['question', 'answer']

class TestimonialAnswerAdmin(admin.ModelAdmin):
	menu_title = "Testimonial Answer"
	menu_group = "Feedback"
	list_display = ['question', 'answer']
		

admin.site.register(Testimonial, TestimonialAdmin)
admin.site.register(Questionnaire, QuestionnaireAdmin)
admin.site.register(QuestionnaireAnswer, QuestionnaireAnswerAdmin)
admin.site.register(TestimonialAnswer, TestimonialAnswerAdmin)
admin.site.register(TestimonialCategory)
admin.site.register(QuestionnaireCategory)

