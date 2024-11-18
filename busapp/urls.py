from django.urls import path

from .views import AppuserListView,AppuserDetailView

urlpatterns = [
    path('appuser/', AppuserListView.as_view(), name='appuser-list'),
    path('appuser/<int:pk>/', AppuserDetailView.as_view(), name='appuser-detail'),
]