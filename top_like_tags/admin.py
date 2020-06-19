from django.contrib import admin
from .models import blog_posts, fixed_hashtag, analytics
from django.db import models
from django.forms import TextInput, Textarea


class BlogAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': Textarea(attrs={'rows': 12, 'cols': 80})},
    }

admin.site.register(blog_posts, BlogAdmin)
admin.site.register(fixed_hashtag, BlogAdmin)
admin.site.register(analytics)
