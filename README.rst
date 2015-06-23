.. image:: https://travis-ci.org/zniper/simple-article.svg?branch=master
          :target: https://travis-ci.org/zniper/simple-article

.. image:: https://coveralls.io/repos/zniper/simple-article/badge.svg?branch=master 
          :target: https://coveralls.io/r/zniper/simple-article?branch=master

**simple-article** is a Django application which provides a simple Article model. That model could be a good start for simple blog or news, without the needs for installation much of other 3rd party packages.

Installation
============

You can install simple-article from PyPI::

    pip install simple-article

Or from GitHub::

    pip install https://github.com/zniper/simple-article/zipball/master

Configuration
=============

Inside settings module, put `article` into `INSTALLED_APPS`::

    INSTALLED_APPS = (
        ...
        'article',
    )

Include article URLs inside application urls.py file::

    urlpatterns = patterns(
       ...
        url(r'^blog/', include('article.urls')),
        ...
    )

Then, update the database::

    python manage.py syncdb

or using South::
  
    python manage.py migrate article

Usage
=====

Inside templates, there is an assignment tag named `recent_articles` which returns limited number of newest articles::

    {% load article_tags %}

Short call, with maximum 10 newest articles returned::

    {% recent_articles as other_articles %}

Customized call, with exclusion of given article::
    
    {% recent_articles limit=5 exclude=article.pk as other_articles %}
