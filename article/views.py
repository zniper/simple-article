from django.views.generic import DetailView

from .models import Article


class ArticleView(DetailView):
    model = Article
    template_name = 'article-detail.html'
