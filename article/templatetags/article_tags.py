from django import template

from article.models import Article

register = template.Library()


@register.assignment_tag
def recent_articles(limit=10, exclude=None):
    """Returns list of latest article"""
    queryset = Article.objects.filter(published=True).order_by('-modified')
    if exclude:
        if hasattr(exclude, '__iter__'):
            queryset = queryset.exclude(pk__in=exclude)
        else:
            queryset = queryset.exclude(pk=exclude)
    return queryset
