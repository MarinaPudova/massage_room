from django.urls import path, include

from massage_types import views

urlpatterns = [
    path('massage_types/', views.MassageTypesListView.as_view(), name='types-list'),
    path('massage_types/<int:pk>', views.MassageTypesDetailView.as_view(), name='types-detail'),
    path('massage_types/create', views.MassageTypesCreateView.as_view(), name='type-create'),
    path('massage_types/<int:pk>/update', views.MassageTypesUpdateView.as_view(), name='type-update'),
    path('massage_types/<int:pk>/delete', views.MassageTypesDeleteView.as_view(), name='type-delete'),
]
