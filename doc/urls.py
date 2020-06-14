from django.urls import path
from .views import DocListView
from .views import DocDatailView


urlpatterns = [
    path('list/', DocListView.as_view(), name="doc_list"),
    path('detail/<int:pk>/', DocDatailView.as_view(), name="doc_detail"),
]
