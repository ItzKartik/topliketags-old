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
    path('generator/', views.generator, name='generator'),

    path('only_index/', views.only_index, name='only_index'),
    path('only_popular_hashtags/', views.only_fixed, name='only_fixed_hashtag'),
    path('only_hashtag_tips/', views.only_forums, name='only_forums'),
    path('only_about/', views.only_about, name='only_about'),
    path('only_policy/', views.only_policy, name='only_policy'),
    path('only_contact/', views.only_contact, name='only_contact'),
    re_path('only_blog/(?P<blog_id>[\w-]+)', views.only_full_blog, name='only_full_blog'),

    re_path('blog/(?P<blog_id>[\w-]+)', views.full_blog, name='full_blog'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
