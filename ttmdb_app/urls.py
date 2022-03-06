from django.urls import path
from . import views

urlpatterns = [
    path('ttmdb_app/', views.index)      # domain for ttmdb_app index
]