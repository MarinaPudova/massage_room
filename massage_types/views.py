from django.shortcuts import render
from django.views import generic

from massage_types.models import MassageType


# Create your views here.


class MassageTypesListView(generic.ListView):
    model = MassageType
    template_name = 'types/types_list.html'
    context_object_name = 'types'
    ordering = 'name'
    # paginate_by = 4


class MassageTypesDetailView(generic.DetailView):
    model = MassageType
    template_name = 'types/types_detail.html'
    context_object_name = 'type'
