from django.urls import path
from . import views
    
urlpatterns = [
    path('classes/<str:course_name>/', views.course_detail),
]