from django.urls import path
from . import views

urlpatterns = [
    path('', views.puzzles_root_redirect, name='puzzles_root'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('export-csv/', views.export_csv, name='export_csv'),
    path('toggle-solved/', views.toggle_solved, name='toggle_solved'),
] 