from django.db import models


class blog_posts(models.Model):
    blogimg = models.FileField(null=False, blank=False)
    blogurl = models.CharField(max_length=100)
    seotitle = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000)
    keyword = models.CharField(max_length=1000)
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=2000)

    def __str__(self):
        return self.title


class fixed_hashtag(models.Model):
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=200, blank=True, null=True)
    hashtags = models.CharField(max_length=2000)

    def __str__(self):
        return self.title