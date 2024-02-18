from django.urls import path, include

from massage_types import views

urlpatterns = [
    path('massage_types/', views.MassageTypesListView.as_view(), name='types-list'),
    path('massage_types/<int:pk>', views.MassageTypesDetailView.as_view(), name='types-detail'),
]
