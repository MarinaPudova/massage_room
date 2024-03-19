from django.shortcuts import render
from django.urls import reverse
from django.views import generic

from massage_types.forms import MassageTypeForm
from massage_types.models import MassageType


# Create your views here.


class MassageTypesListView(generic.ListView):
    model = MassageType
    template_name = 'types/types_list.html'
    context_object_name = 'types'
    # ordering = 'name'
    # paginate_by = 4


class MassageTypesDetailView(generic.DetailView):
    model = MassageType
    template_name = 'types/types_detail.html'
    context_object_name = 'type'


class MassageTypesCreateView(generic.CreateView):
    template_name = 'types/types_create.html'
    form_class = MassageTypeForm

    def get_success_url(self):
        return reverse('types-list')


class MassageTypesUpdateView(generic.UpdateView):
    model = MassageType
    template_name = 'types/types_update.html'
    form_class = MassageTypeForm

    def get_success_url(self):
        return reverse('types-list')


class MassageTypesDeleteView(generic.DeleteView):
    model = MassageType
    template_name = 'types/types_delete.html'

    def get_success_url(self):
        return reverse('types-list')
