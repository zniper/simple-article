from django.test import TestCase
from django.core.urlresolvers import reverse

from .templatetags import article_tags
from .models import Article


class ArticleModelTests(TestCase):

    def test_save(self):
        article = Article(title='Single One', summary='', body='Content')
        article.save()
        self.assertGreater(article.pk, 0)
        self.assertEqual(article.slug, 'single-one')
        self.assertEqual(str(article), 'Article: Single One')

    def test_duplicate(self):
        a0 = Article(title='Single One', summary='', body='Content')
        a0.save()
        a1 = Article(title='Single One', summary='', body='Content 2')
        a1.save()
        self.assertEqual(a1.slug, 'single-one-1')


class ArticleListViewTests(TestCase):

    fixtures = ['articles.json']

    def test_normal(self):
        res = self.client.get(reverse('article-list'))
        self.assertEqual(res.status_code, 200)


class ArticleViewTests(TestCase):

    fixtures = ['articles.json']

    def test_normal(self):
        res = self.client.get(reverse(
            'article-detail', kwargs={'slug': 'the-first-article'}))
        self.assertEqual(res.status_code, 200)


class TemplateTagsTests(TestCase):

    fixtures = ['articles.json']

    def test_normal(self):
        queryset = article_tags.recent_articles()
        self.assertEqual(queryset.count(), 2)

    def test_exclude(self):
        queryset = article_tags.recent_articles(exclude=1)
        self.assertEqual(queryset.count(), 1)

    def test_exclude_multi(self):
        queryset = article_tags.recent_articles(exclude=[1, 2])
        self.assertEqual(queryset.count(), 1)


class ImportTests(TestCase):

    def test_admin(self):
        # weird?
        import admin
        self.assertEqual(1, 1)
