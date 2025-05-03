from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet

router = DefaultRouter()

router.register('todos', TaskViewSet, basename='todos')

urlpatterns = [
    path('', include(router.urls))
]
