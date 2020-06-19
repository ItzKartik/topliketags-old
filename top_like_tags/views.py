import json
import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from .models import blog_posts, fixed_hashtag, analytics
from top_like_tags import models
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render, redirect
from bs4 import BeautifulSoup
import requests
from django.views.generic.base import View


def about(request):
    m = models.about.objects.get(id=1)
    return render(request, 'top_like_tags/about.html', {'seo': m})

def policy(request):
    m = models.policy.objects.get(id=1)
    return render(request, 'top_like_tags/about.html', {'seo': m})

def index(request):
    m = models.home.objects.get(id=1)
    a = analytics.objects.get(id=1)
    a.home_page = a.home_page+1
    a.save()
    model = blog_posts.objects.all()
    if len(model) < 4:
        pass
    else:
        model = model[:4]
    data = {
        'blog': model,
        'seo': m
    }
    return render(request, 'top_like_tags/index.html', data)


def fixed(request):
    m = models.fixed_hashtag.objects.get(id=1)
    a = analytics.objects.get(id=1)
    a.popular_hashtag = a.popular_hashtag+1
    a.save()
    model = fixed_hashtag.objects.all()
    data = {
        'fixed_hash': model,
        'seo': m
    }
    return render(request, 'top_like_tags/fixed_hashtag.html', data)


def full_blog(request, blog_id):
    a = analytics.objects.get(id=1)
    a.full_blog = a.full_blog+1
    a.save()
    model = blog_posts.objects.get(blogurl=blog_id)
    return render(request, 'top_like_tags/full_blog.html', {'blog': model})


def forums(request):
    m = models.hashtag_tips.objects.get(id=1)

    a = analytics.objects.get(id=1)
    a.forums = a.forums+1
    a.save()
    model = blog_posts.objects.all()
    data = {
        'blog': model,
        'seo': m
    }
    return render(request, 'top_like_tags/forums.html', data)


class generator(View):
    def post(self, *args, **kwargs):
        hashtag = self.request.POST['keyword']
        random_text = self.request.POST['random']
        min_posts = None
        max_posts = None
        search_url = 'https://www.instagram.com/web/search/topsearch/'
        explore_headers = {'Host': 'www.instagram.com',
                                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0',
                                'Accept': '*/*',
                                'Accept-Language': 'en-US;q=0.7,en;q=0.3',
                                'Accept-Encoding': 'gzip, deflate, br',
                                'X-Requested-With': 'XMLHttpRequest',
                                'Referer': 'https://www.instagram.com/',
                                'Connection': 'keep-alive'}
        if hashtag[0] != '#':
            hashtag = '#' + hashtag
        params = {'context': 'blended',
                  'query': hashtag,
                  'rank_token': random.uniform(0, 1)}
        response = self.get_request(search_url, params=params, headers=explore_headers)
        tag_list = response.json()['hashtags']
        tags = []
        for tag in tag_list:
            if min_posts:
                if tag['hashtag']['media_count'] < min_posts:
                    continue
            if max_posts:
                if tag['hashtag']['media_count'] > max_posts:
                    continue
            tags.append(tag['hashtag']['name'])
        if int(random_text) == 1:
            tag = tags[30:]
        elif len(tags) > 30:
            tag = tags[:30]
        elif len(tags) <= 30:
            tag = tags
        else:
            tag = tags
        return HttpResponse(json.dumps(tag))

    def get_request(self, url, params=None, **kwargs):
        """Make a GET request"""
        self.s = requests.Session()
        request = self.s.get(url, params=params, **kwargs)
        return self.analyze_request(request)

    def analyze_request(self, request):
        """Check if the request was successful"""
        if request.status_code == 200:
            return request
        else:
            raise requests.HTTPError(str(request.status_code))


def contact(request):
    if request.method == 'POST':
        name = request.POST['id_name']
        email = request.POST['id_email']
        message = request.POST['id_msg']

        msg = MIMEMultipart('alternative')
        msg['Subject'] = 'New Email from TopLikeTags.com'
        html = """
            <html>
              <head></head>
              <body>
                <h1>Hi Admin</h1>
                <p>You Just Got An Email From %s. Please Mail Him Back On %s.</p>
                <p>Message : %s</p>
              </body>
            </html>
            """ % (name, email, message)
        part2 = MIMEText(html, 'html')
        msg.attach(part2)
        smtp_server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        smtp_server.login('topliketags@gmail.com', 'Helloworld20,')
        smtp_server.sendmail("topliketags@gmail.com", 'topliketags@gmail.com', msg.as_string())
        smtp_server.close()
        return redirect('top_like_tags:index')
    else:
        m = models.contact_page.objects.get(id=1)
        
        a = analytics.objects.get(id=1)
        a.contact = a.contact+1
        a.save()
        data = {
            'seo': m
        }
        return render(request, 'top_like_tags/contact.html')
