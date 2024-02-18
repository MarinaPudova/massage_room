from django.urls import path

from massage_masters import views

urlpatterns = [
    path('massage_masters/', views.MassageMastersListView.as_view(), name='masters-list'),
    path('massage_masters/<int:pk>', views.MassageMastersDetailView.as_view(), name='masters-detail'),
]
