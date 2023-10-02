from django.urls import path
from first_app import views

urlpatterns = [
    path("index/", views.index, name="index"),
    path("basic_app/index",views.list_fUser,name='bsindex'),
    path("basic_app/form",views.form_name_view,name='form'),
]
