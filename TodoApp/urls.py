from django.urls import path

from .views import HomeView, CreateTaskView,TodolistView,TaskUpdateView,TaskDeleteView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("create",CreateTaskView.as_view(),name="create"),
    path("list",TodolistView.as_view(),name ='list'),
    path("update/<int:pk>",TaskUpdateView.as_view(),name="update"),
    path("delete/<int:pk>",TaskDeleteView.as_view(), name = "delete")
]
