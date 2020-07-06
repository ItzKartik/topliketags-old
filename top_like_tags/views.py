import requests
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
from django.views.generic.base import View

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
from top_like_tags.insta_login import insta_login

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

def generator(request):
    hashtag = request.POST['keyword']
    random = request.POST['random']
    if ' ' in hashtag:
        h = hashtag.split(' ')
        hashtag = "".join([i for i in h])
    else:
        pass
    if '#' in hashtag:
        pass
    else:
        hashtag = '#'+hashtag
    return HttpResponse(hashtag)
    # d = insta_login()
    # d = d[0]

    ctextarea = WebDriverWait(d, 20).until(EC.element_to_be_clickable((By.XPATH, 
    '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')))
    ctextarea = d.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
    ctextarea.clear()
    ActionChains(d).move_to_element(ctextarea).click(ctextarea).send_keys(hashtag).perform()

    sleep(1)
    fetched_hashtags = []
    for elem in d.find_elements_by_xpath('.//span'):
        fetched_hashtags.append(elem.get_attribute("innerHTML"))
    hashtags = []
    for i in fetched_hashtags:
        if i == '':
            pass
        elif hashtag in i:
            hashtags.append(i+' ')
        else:
            pass
    if random == 1:
        random.shuffle(hashtags)
    else:
        pass
    return HttpResponse(hashtags)

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
