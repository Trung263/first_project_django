from django.urls import path
from task3 import views

urlpatterns = [
    path("users/", views.user_list, name="users")
]
