from django.urls import path

from info_news import views

urlpatterns = [
    path('', views.site_description, name='site_description'),
    path('contacts/', views.site_info_about, name='site_info_about'),
]
