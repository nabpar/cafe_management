from django.urls import path
from .views import CmsListCreateView,CmsDetailView


urlpatterns = [
    path('cms/',CmsListCreateView.as_view(), name='cms-list-create'),
    path('cms/<int:pk>/', CmsDetailView.as_view(), name='cms-detail'),
]

