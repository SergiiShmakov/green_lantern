from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, FormView
from django.core import serializers

from src.apps.articles.models import Article
from src.apps.articles.forms import ArticlesForm


def main_page(request):
    return render(request, 'pages/main_page.html')


class SearchResultsView(View):
    def get(self, request, **kwargs):
        # form = SearchForm(data=request.GET)
        search_q = request.GET.get('search', '')
        if search_q:
            articles = Article.objects.filter(title__icontains=search_q)
        else:
            articles = Article.objects.all()

        context_data = {
            'articles': articles,
            # 'search_form': form
        }
        return render(request, 'pages/search.html', context=context_data)


def article_json(request, id):
    return HttpResponse(serializers.serialize('json', [Article.objects.get(pk=id)]))


def articles_list_json(request):
    return JsonResponse(list(Article.objects.all().values()), safe=False)


class ArticlesListView(ListView):
    model = Article
    template_name = 'articles.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)


class ArticlesFormView(FormView):
    template_name = 'articles_form.html'
    form_class = ArticlesForm
    success_url = '/articles/search/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
