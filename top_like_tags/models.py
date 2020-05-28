from django.db import models


class blog_posts(models.Model):
    blogimg = models.FileField(null=False, blank=False)
    b_url = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=2000)

    def __str__(self):
        return self.title


class fixed_hashtag(models.Model):
    title = models.CharField(max_length=100)
    hashtags = models.CharField(max_length=2000)

    def __str__(self):
        return self.title