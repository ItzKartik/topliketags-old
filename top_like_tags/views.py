import browser_cookie3
import requests
import json
import os
import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from .models import blog_posts, fixed_hashtag, analytics
from top_like_tags import models
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.base import View

import os
from django.conf import settings

from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import ui
from selenium.webdriver.common.by import By
from django.http import HttpResponse

def about(request):
    m = models.about.objects.all().first()
    return render(request, 'top_like_tags/about.html', {'seo': m})

def policy(request):
    m = models.policy_page.objects.all().first()
    return render(request, 'top_like_tags/policy.html', {'seo': m})

def index(request):
    m = models.home.objects.all().first()
    a = analytics.objects.all().first()
    a.home_page = a.home_page+1
    a.save()
    model = blog_posts.objects.all().order_by('-date')
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
    m = models.fixed_hashtag.objects.all().first()
    a = analytics.objects.all().first()
    a.popular_hashtag = a.popular_hashtag+1
    a.save()
    model = fixed_hashtag.objects.all()
    data = {
        'fixed_hash': model,
        'seo': m
    }
    return render(request, 'top_like_tags/fixed_hashtag.html', data)


def full_blog(request, blog_id):
    a = analytics.objects.all().first()
    a.full_blog = a.full_blog+1
    a.save()
    model = blog_posts.objects.get(blogurl=blog_id)
    return render(request, 'top_like_tags/full_blog.html', {'blog': model})


def forums(request):
    m = models.hashtag_tips.objects.all().first()

    a = analytics.objects.all().first()
    a.forums = a.forums+1
    a.save()
    model = blog_posts.objects.all().order_by('-date')
    data = {
        'blog': model,
        'seo': m
    }
    return render(request, 'top_like_tags/forums.html', data)

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
        smtp_server.login('topliketagscontact@gmail.com', 'Helloworld20,')
        smtp_server.sendmail("topliketagscontact@gmail.com", 'topliketags@gmail.com', msg.as_string())
        smtp_server.close()
        # return redirect('top_like_tags:index')
        remark = 'Your message has been sent.'
        return render(request, 'top_like_tags/contact.html', {'remark': remark})
    else:
        m = models.contact_page.objects.all().first()
        
        a = analytics.objects.all().first()
        a.contact = a.contact+1
        a.save()
        data = {
            'seo': m
        }
        return render(request, 'top_like_tags/contact.html')


def generator(request):
    path_of_file = os.path.join(settings.BASE_DIR, 'static')
    full_path = path_of_file+'/topliketags-profile/Default/Cookies'
    cookies = browser_cookie3.chrome(cookie_file=full_path)
    hashtag = request.POST['keyword']
    random_text = request.POST['random']
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

    s = requests.Session()
    request = s.get(search_url, params=params, verify=False, headers=explore_headers, cookies=cookies, timeout=3)
    response = None
    if request.status_code == 200:
        response = request
    else:
        raise requests.HTTPError(str(request.status_code))
    tag_list = response.json()['hashtags']
    tags = []

    for tag in tag_list:
        if tag == '':
            pass
        else:
            tags.append('#'+tag['hashtag']['name']+' ')
    if int(random_text) == 1:
        return HttpResponse(random.sample(tags, 30))
    return HttpResponse(tags[30:])

