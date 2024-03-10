from django.urls import path, include

from client_comments import views

urlpatterns = [
    path('comments/create/<int:pk>', views.ClientCommentCreateView.as_view(), name='comment-create'),
]
