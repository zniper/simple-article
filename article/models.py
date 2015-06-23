from datetime import datetime

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify

from tinymce.models import HTMLField
from taggit.managers import TaggableManager


class Article(models.Model):
    """Simple article model with basic fields"""
    title = models.CharField(_('Title'), max_length=255)
    slug = models.SlugField(_('Slug'), max_length=255, unique=True, blank=True)
    summary = models.TextField(_('Summary'), null=True, blank=True)
    image = models.ImageField(_('Image'), blank=True, null=True,
                              upload_to='articles/%Y/%m/%d')
    modified = models.DateTimeField(_('Modified'), default=datetime.now)
    published = models.BooleanField(default=False)
    body = HTMLField(_('Body'))
    tags = TaggableManager()

    class Meta:
        ordering = ['-modified']
        verbose_name = 'Article'

    def __unicode__(self):
        return 'Article: %s' % self.title

    def get_absolute_url(self):
        return reverse('article-detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slug = slugify(self.title)
            counter = 1
            while self.__class__.objects.filter(slug=self.slug).exists():
                self.slug = '{0}-{1}'.format(slug, counter)
            counter += 1
        return super(Article, self).save(*args, **kwargs)
