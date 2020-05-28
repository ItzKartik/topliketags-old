from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('top_like_tags.urls')),
    path('admin/', admin.site.urls),
]
