from django.urls import path

from User import views

urlpatterns = [
    path('index/', views.index),
    path('addstudent/', views.add_student),
    path('getstudents/', views.get_students),
    path('updatestudents/', views.updatestudents),
    path('deletestudents/', views.deletestudents)
]