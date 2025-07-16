
from django.shortcuts import redirect
from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('', lambda request: redirect('/puzzles/dashboard/')),
    path('admin/', admin.site.urls),
    path('puzzles/', include('puzzles.urls')),
]
