from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('decades', views.DecadeList.as_view(), name='decade_list'),
    path('decades/<int:pk>', views.DecadeDetail.as_view(), name='decade_detail'),
    path('fads', views.FadList.as_view(), name='fad_list'),
    path('fads/<int:pk>', views.FadDetail.as_view(), name='fad_detail')
]