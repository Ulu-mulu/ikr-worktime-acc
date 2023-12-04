from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from main import views


schema_view = get_schema_view(
   openapi.Info(
      title="Worktime accounting",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


router = DefaultRouter()
router.register(r'cameras', views.CameraViewSet, basename='camera')
router.register(r'tags', views.TagViewSet, basename='tag')
router.register(r'images', views.ImageViewSet, basename='image')
router.register(r'statistics', views.StatisticViewSet, basename='statistic')
router.register(r'models', views.ModelViewSet, basename='model')
router.register(r'slices', views.SliceViewSet, basename='slice')
router.register(r'events', views.EventViewSet, basename='event')


urlpatterns = [
    path('', include(router.urls)),
    path(
        'swagger<format>/',
        schema_view.without_ui(cache_timeout=0),
        name='schema-json'
    ),
    path(
        'swagger/',
        schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui'
    ),
    path(
        'redoc/',
        schema_view.with_ui('redoc', cache_timeout=0),
        name='schema-redoc'
    ),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
]
