from django.db import models


class home(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=3000)
    keywords = models.CharField(max_length=3000)

class about(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=3000)
    keywords = models.CharField(max_length=3000)

class hashtag_tips(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=3000)
    keywords = models.CharField(max_length=3000)

class most_popular_hashtags(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=3000)
    keywords = models.CharField(max_length=3000)

class contact_page(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=3000)
    keywords = models.CharField(max_length=3000)

class policy_page(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=3000)
    keywords = models.CharField(max_length=3000)

class blog_posts(models.Model):
    blogimg = models.FileField(null=False, blank=False)
    blogurl = models.CharField(max_length=100)
    seotitle = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000)
    keyword = models.CharField(max_length=1000)
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=2000)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class fixed_hashtag(models.Model):
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=200, blank=True, null=True)
    hashtags = models.CharField(max_length=2000)

    def __str__(self):
        return self.title


class analytics(models.Model):
    home_page = models.IntegerField()
    popular_hashtag = models.IntegerField()
    forums = models.IntegerField()
    full_blog = models.IntegerField()
    contact = models.IntegerField()