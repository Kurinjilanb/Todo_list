from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import TaskViewset

routers = DefaultRouter()

routers.register("task", TaskViewset, basename="taskviewset")

urlpatterns = []


urlpatterns += routers.urls
