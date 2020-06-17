from django.urls import path

from src.apps.articles.views import main_page, SearchResultsView, article_json, articles_list_json, ArticlesListView, \
    ArticlesFormView

app_name = 'articles'

urlpatterns = [
    path('search/', main_page, name='main-page'),
    path('results/', SearchResultsView.as_view(), name='search-results'),
    path('json/', article_json, name='json-article-list'),
    path('json_list/', articles_list_json, name='json-article-list'),
    path('articles_list/', ArticlesListView.as_view(), name='articles-list'),
    path('articles_form/', ArticlesFormView.as_view(), name='articles-form'),

]
