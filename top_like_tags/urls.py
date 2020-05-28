from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from top_like_tags import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'top_like_tags'

urlpatterns = [
    path('', views.index, name='index'),
    path('popular_hashtags/', views.fixed, name='fixed_hashtag'),
    path('forums/', views.forums, name='forums'),
    path('about/', TemplateView.as_view(template_name='top_like_tags/about.html'), name='about'),
    path('contact/', views.contact, name='contact'),
    re_path('blog/(?P<blog_id>[\w-]+)', views.full_blog, name='full_blog'),
    path('generator/', views.generator.as_view(), name='generator'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)