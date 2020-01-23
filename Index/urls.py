from django.urls import path

from Index import views

urlpatterns = [
    path('index/', views.index)
]