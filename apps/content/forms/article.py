from django.forms import ModelForm
from content.models.article import Article, ArticleCategory
from django.forms.widgets import CheckboxSelectMultiple

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        exclude = ['state', 'publish_date', 'author', 'slug']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["category"].widget = CheckboxSelectMultiple()
        self.fields["category"].queryset = ArticleCategory.objects.all()
