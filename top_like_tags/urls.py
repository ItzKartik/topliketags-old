from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from top_like_tags import views
from django.conf.urls.static import static
from django.conf import settings
from top_like_tags import models


app_name = 'top_like_tags'


urlpatterns = [
    path('', views.index, name='index'),
    path('popular_hashtags/', views.fixed, name='fixed_hashtag'),
    path('hashtag_tips/', views.forums, name='forums'),
    path('about/', views.about, name='about'),
    path('policy/', views.policy, name='policy'),
    path('contact/', views.contact, name='contact'),
    re_path('blog/(?P<blog_id>[\w-]+)', views.full_blog, name='full_blog'),
    # path('generator/', views.generator.as_view(), name='generator'),
    path('generator/', views.generator, name='generator'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
