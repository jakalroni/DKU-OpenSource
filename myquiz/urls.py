from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('quiz/<int:id>/', views.quiz),
    path('result/<int:id>/', views.result),
    path('stats/', views.stats)
]