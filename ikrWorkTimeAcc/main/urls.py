from django.urls import path
from main import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('cameras/', views.CameraList.as_view()),
    path('cameras/<int:pk>/', views.CameraDetailed.as_view()),
    path('tags/', views.TagList.as_view()),
    path('tags/<int:pk>/', views.TagDetailed.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
