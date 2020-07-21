from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', include('top_like_tags.urls')),
    path(
        "ads.txt",
        RedirectView.as_view(url=staticfiles_storage.url("ads.txt")),
    ),
    path(
        "sitemap.xml",
         RedirectView.as_view(url=staticfiles_storage.url("sitemap.xml")),
    ),
    path('oneandonly/', admin.site.urls),
]
