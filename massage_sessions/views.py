from django.shortcuts import render
from django.urls import reverse
from django.views import generic

from massage_sessions.forms import MassageSessionAdminForm, MassageSessionForm
from massage_sessions.models import MassageSession

# Create your views here.

#
# path('massage-sessions/', views.NewsListView.as_view(), name='massage-sessions-list'),
# path('massage-session/<int:pk>', views.NewsDetailView.as_view(), name='massage-session-detail'),
# path('massage-session/create', views.NewsCreateView.as_view(), name='massage-session-create'),
# path('massage-session/<int:pk>/update', views.NewsUpdateView.as_view(), name='massage-session-update'),


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
#
#     def form_valid(self, form):
#         comment = form.save(commit=False)
#         comment.master = MassageMaster.objects.get(pk=self.kwargs.get('pk'))
#         comment.save()
#         return super().form_valid(form)
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['master_url'] = MassageMaster.objects.get(pk=self.kwargs.get('pk'))
#         return context
#
#
# class MassageSessionCreateView(generic.CreateView):
#     template_name = 'news/news_create.html'
#     form_class = NewsForm
#
#     def get_success_url(self):
#         return reverse('news-list')
