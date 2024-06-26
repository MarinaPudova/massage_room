from django.shortcuts import render
from django.views import generic

from massage_masters.models import MassageMaster


# Create your views here.


class MassageMastersListView(generic.ListView):
    # model = MassageMaster
    template_name = 'masters/masters_list.html'
    context_object_name = 'masters'
    queryset = MassageMaster.objects.filter(is_working=True)


class MassageMastersDetailView(generic.DetailView):
    model = MassageMaster
    template_name = 'masters/masters_detail.html'
    context_object_name = 'master'


class MassageMastersCommentsDetailView(generic.DetailView):
    model = MassageMaster
    template_name = 'comments/comment_list.html'
    context_object_name = 'master'
