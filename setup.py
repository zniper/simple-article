from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='simple-article',
    version='0.2.0',
    description='Provide deadly simple Article model for Django',
    long_description=long_description,
    url='https://github.com/zniper/simple-article',
    author='Ha Pham',
    author_email='me.zniper@gmail.com',
    license='MIT',
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    keywords='article model simple django entry blog',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    install_requires=['django-tinymce', 'Pillow', 'django-taggit',
                      'django-nose'],
    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },
)
