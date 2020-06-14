from django.urls import path
from .views import ColaboratorListView


urlpatterns = [
    path('list/', ColaboratorListView.as_view(), name='colaborator_list'),
]
