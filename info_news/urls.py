from django.urls import path

from info_news import views

urlpatterns = [
    path('', views.site_description, name='site_description'),
    path('contacts/', views.site_info_about, name='site_info_about'),
    path('news/', views.NewsListView.as_view(), name='news-list'),
    path('news/<int:pk>', views.NewsDetailView.as_view(), name='news-detail'),
    path('news/create', views.NewsCreateView.as_view(), name='news-create'),
    path('news/<int:pk>/update', views.NewsUpdateView.as_view(), name='news-update'),
    path('news/<int:pk>/delete', views.NewsDeleteView.as_view(), name='news-delete'),
]
