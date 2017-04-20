"""
Based entirely on Django's own ``setup.py``.
"""
import os
from setuptools import setup, find_packages

import tagging



def fullsplit(path, result=None):
    """
    Split a pathname into components (the opposite of os.path.join) in a
    platform-neutral way.
    """
    if result is None:
        result = []
    head, tail = os.path.split(path)
    if head == '':
        return [tail] + result
    if head == path:
        return result
    return fullsplit(head, [tail] + result)


setup(
    name = 'django-tagging',
    version = tagging.get_version(),
    description = 'Generic tagging application for Django',
    author = 'Jonathan Buchanan',
    author_email = 'jonathan.buchanan@gmail.com',
    url = 'http://code.google.com/p/django-tagging/',
    packages=find_packages(),
    include_package_data=True,

    classifiers = ['Development Status :: 4 - Beta',
                   'Environment :: Web Environment',
                   'Framework :: Django',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Utilities'],
)
