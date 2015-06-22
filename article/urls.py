from django.conf.urls import url, patterns

from .views import ArticleView


urlpatterns = patterns(
    '',
    url('article/(?P<slug>[a-z0-9-]+)/$',
        ArticleView.as_view(), name='article-detail'),
)
