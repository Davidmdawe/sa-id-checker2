from django.contrib import admin
from django.urls import path, include

# sa_id_checker/urls.py

urlpatterns = [
    path('admin/', admin.site.urls),
    #Home id_check app URLs
    path('', include('id_check.urls')),  
]
