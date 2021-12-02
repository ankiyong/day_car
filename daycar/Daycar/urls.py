
from django.contrib import admin
from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
    path('dash/',include('dashboard.urls')),
]
