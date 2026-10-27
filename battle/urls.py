from django.urls import path
from . import views
urlpatterns = [path("", views.arena, name="arena"), path("restart/", views.new_battle, name="restart")]
