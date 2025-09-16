"""Test urls for tagging."""
from django.urls import path, re_path

from tagging.views import TaggedObjectList
from tagging.tests.models import Article


class StaticTaggedObjectList(TaggedObjectList):
    tag = 'static'
    queryset = Article.objects.all()


urlpatterns = [
    path('static/', StaticTaggedObjectList.as_view()),
    path('static/related/', StaticTaggedObjectList.as_view(
        related_tags=True)),
    path('no-tag/', TaggedObjectList.as_view(model=Article)),
    path('no-query-no-model/', TaggedObjectList.as_view()),
    re_path(r'^(?P<tag>[^/]+(?u))/$', TaggedObjectList.as_view(model=Article)),
]
