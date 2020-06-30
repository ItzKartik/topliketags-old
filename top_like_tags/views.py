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

import requests
class generator(View):
    def post(self, *args, **kwargs):
        d = insta_login()
        d = d[0]
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

# def generator(request):
#     hashtag = request.POST['keyword']
#     random = request.POST['random']
#     if '#' in hashtag:
#         pass
#     else:
#         hashtag = '#'+hashtag
#     d = insta_login()
#     d = d[0]

#     ctextarea = WebDriverWait(d, 20).until(EC.element_to_be_clickable((By.XPATH, 
#     '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')))
#     ctextarea = d.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
#     ctextarea.clear()
#     ActionChains(d).move_to_element(ctextarea).click(ctextarea).send_keys(hashtag).perform()

#     sleep(4)
#     fetched_hashtags = []
#     elems = d.find_elements_by_xpath('//span')
#     for elem in elems:
#         fetched_hashtags.append(elem.get_attribute("innerHTML"))
#     hashtaglist = fetched_hashtags[:len(fetched_hashtags)-2]
#     hashtags = []
#     for i in hashtaglist:
#         if i == '':
#             pass
#         elif '#' in i:
#             hashtags.append(i+' ')
#         else:
#             pass
#     if random == 1:
#         random.shuffle(hashtags)
#     else:
#         pass
#     h = []
#     if len(hashtags) > 30:
#         h = hashtags[:30]
#     else:
#         h = hashtags
#     return HttpResponse(h)

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
