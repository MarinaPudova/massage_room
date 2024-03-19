from django.urls import path

from massage_sessions import views

urlpatterns = [
    path('massage-sessions/', views.MassageSessionListView.as_view(), name='massage-sessions-list'),
    path('massage-session/<int:pk>', views.MassageSessionDetailView.as_view(), name='massage-session-detail'),
    path('massage-session/create', views.MassageSessionCreateView.as_view(), name='massage-session-create'),
    path('massage-session/<int:pk>/update', views.MassageSessionUpdateView.as_view(), name='massage-session-update'),
    # path('news/<int:pk>/delete', views.NewsDeleteView.as_view(), name='news-delete'),
]
