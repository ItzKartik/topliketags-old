from django.contrib import admin
from .models import blog_posts, fixed_hashtag, analytics, home, about, hashtag_tips, most_popular_hashtags, policy_page, contact_page
from django.db import models
from django.forms import TextInput, Textarea


class BlogAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': Textarea(attrs={'rows': 12, 'cols': 80})},
    }

admin.site.register(home)
admin.site.register(about)
admin.site.register(hashtag_tips)
admin.site.register(most_popular_hashtags)
admin.site.register(contact_page)
admin.site.register(policy_page)

admin.site.register(blog_posts, BlogAdmin)
admin.site.register(fixed_hashtag, BlogAdmin)
admin.site.register(analytics)