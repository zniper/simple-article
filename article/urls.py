from django.conf.urls import url, patterns

from .views import ArticleListView, ArticleView


urlpatterns = patterns(
    '',
    url('^$', ArticleListView.as_view(), name='article-list'),
    url('^article/(?P<slug>[a-z0-9-]+)/$',
        ArticleView.as_view(), name='article-detail'),
)
