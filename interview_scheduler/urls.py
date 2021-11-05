from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views

from scheduler.views import CustomAuthToken

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', CustomAuthToken.as_view()),
    path(r'', include('scheduler.urls')),
]
