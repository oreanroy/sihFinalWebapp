from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('check/', views.check, name='check'),
    path('check/compoundA', views.compoundA, name='compoundA'),
    path('<int:result_id>/', views.result, name='result')
]