"""
Tagging related views.
"""
from django.http import Http404
from django.utils.translation import ugettext as _
from django.views.generic import ListView
from tagging.models import Tag, TaggedItem
from tagging.utils import get_tag


class TagListView(ListView):

    queryset_or_model = None

    def get_queryset(self):
        tag = self.kwargs['tag']
        self.tag_instance = get_tag(tag)
        if self.tag_instance is None:
            raise Http404(_('No Tag found matching "%s".') % tag)
        return TaggedItem.objects.get_by_model(
            self.queryset_or_model, self.tag_instance
        )

    def get_context_data(self, **kwargs):
        context = super(TagListView, self).get_context_data(**kwargs)
        context['tag'] = self.tag_instance
        return context
