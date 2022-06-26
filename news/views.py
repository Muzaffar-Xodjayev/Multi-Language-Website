import requests,json
from django.shortcuts import render,get_object_or_404
from .models import *
from django.contrib.auth.models import User


def homepage(request):
    data = Article.objects.all()
    context = {"data":data}
    return render(request,'home.html',context)

def about(request):
    return render(request,'about.html')


def contact(request):
    return render(request,'contact.html')


def post_detail(request,slug):
    data = get_object_or_404(Article, slug=slug)
    context = {"data":data}
    return render(request,'post_detail.html',context)


def signup(request):
    context={}
    if request.method == 'POST':
        captcha_token =  request.POST['g-recaptcha-response']
        captcha_url = "https://www.google.com/recaptcha/api/siteverify"
        captcha_secret = "6Ldiq6AgAAAAAC7rLjY9i-Y8FWUpv3iYYzspbuFK"
        capthca_data = {"secret":captcha_secret, "response":captcha_token}
        captcha_server_response = requests.post(url=captcha_url, data=capthca_data)
        captcha_json = json.loads(captcha_server_response.text)
        if captcha_json['success']==False:
            context['status'] = 'Invalid reCAPTCHA !!!'
            context['col'] = 'alert-danger'
            return render(request, 'signup.html', context)
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            context['status'] = 'This username already exists !!!'
            context['col'] = 'alert-danger'
        else:
            usr = User.objects.create_user(username=username, email=email, password=password)
            usr.save()
            context['status']= 'You successfully signed up !!!'
            context['col'] = 'alert-success'
    return render(request, 'signup.html', context)




