from django.views.generic import DetailView, ListView
from django.conf import settings

from .models import Article


class ArticleView(DetailView):
    model = Article
    template_name = 'article/detail.html'


class ArticleListView(ListView):
    model = Article
    template_name = 'article/list.html'
    paginate_by = getattr(settings, 'ARTICLE_PAGINATE_BY', None)

    def get_queryset(self):
        queryset = super(ArticleListView, self).get_queryset()
        return queryset.filter(published=True)
