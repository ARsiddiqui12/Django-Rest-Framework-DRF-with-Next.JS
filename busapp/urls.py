from django.urls import path

from .views import AppuserListView,AppuserDetailView,BusinfoListView,BusinfoDetailView

urlpatterns = [
    path('appuser/', AppuserListView.as_view(), name='appuser-list'),
    path('appuser/<int:pk>/', AppuserDetailView.as_view(), name='appuser-detail'),

    path('businfo/', BusinfoListView.as_view(), name='businfo-list'),
    path('businfo/<int:pk>/', BusinfoDetailView.as_view(), name='businfo-detail'),
]