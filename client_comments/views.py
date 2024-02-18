from django.shortcuts import render
from django.urls import reverse
from django.views import generic

from client_comments.forms import ClientCommentForm
from massage_masters.models import MassageMaster


# Create your views here.


class ClientCommentCreateView(generic.CreateView):
    template_name = 'comments/comment_create.html'
    form_class = ClientCommentForm

    def get_success_url(self):
        return reverse('masters-list')

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.master = MassageMaster.objects.get(pk=self.kwargs.get('pk'))
        comment.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['master_url'] = MassageMaster.objects.get(pk=self.kwargs.get('pk'))
        return context
