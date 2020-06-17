from django import forms
from django.forms import ModelForm

from src.apps.articles.models import Article


class SearchForm(forms.Form):
    search = forms.CharField(required=False)


class ArticlesForm(ModelForm):
    class Meta:
        model = Article
        fields = ["title", "body"]


class ArticleImageForm(forms.Form):
    image = forms.ImageField(required=True)
