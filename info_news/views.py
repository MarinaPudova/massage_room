from django.shortcuts import render
from django.views import generic

from info_news.models import News


# Create your views here.


def site_description(request):
    return render(request, 'description.html')


def site_info_about(request):
    return render(request, 'contacts.html')


class NewsListView(generic.ListView):
    model = News
    template_name = 'news/news_list.html'
    context_object_name = 'news'
    ordering = ('-news_date',)


class NewsDetailView(generic.DetailView):
    model = News
    template_name = 'news/news_detail.html'
    context_object_name = 'news_item'
