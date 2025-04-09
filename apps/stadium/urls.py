from django.urls import path
from .views import CreateStadiumView, StadiumDetailView, StadiumListView

urlpatterns = [
    path('create-stadium/', CreateStadiumView.as_view(), name='create-stadium'),
    path('stadium-list/', StadiumListView.as_view(), name='stadium-list'),
    path('stadium-detail/<int:pk>/', StadiumDetailView.as_view(), name='stadium-detail')
]