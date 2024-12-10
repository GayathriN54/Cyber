from django.urls import path
from . import views
from .views import AddModule


app_name = 'blog'

urlpatterns = [
    path("", views.index, name="index" ),
    path("course/<str:module_id>", views.detail, name="detail"),
    path(" ",AddModule.as_view(),name='add_module'),
    
]

