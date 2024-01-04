
from django.contrib import admin
from django.urls import path
from django.urls import path, include
from .views import default

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('main.urls')),

    path('', default),
]
