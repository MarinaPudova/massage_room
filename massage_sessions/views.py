from django.shortcuts import render
from django.urls import reverse
from django.views import generic

from massage_sessions.forms import MassageSessionAdminForm, MassageSessionForm
from massage_sessions.models import MassageSession

# Create your views here.


class MassageSessionListView(generic.ListView):
    model = MassageSession
    template_name = 'sessions/session_list.html'
    context_object_name = 'mas_sessions'
    # ordering = ('-news_date',)


class MassageSessionDetailView(generic.DetailView):
    model = MassageSession
    template_name = 'sessions/session_detail.html'
    context_object_name = 'mas_session_item'


class MassageSessionUpdateView(generic.UpdateView):
    model = MassageSession
    template_name = 'sessions/session_update.html'
    form_class = MassageSessionAdminForm

    def get_success_url(self):
        return reverse('news-list')


class MassageSessionCreateView(generic.CreateView):
    template_name = 'sessions/session_create.html'
    form_class = MassageSessionForm

    def get_success_url(self):
        return reverse('site_info_about')
