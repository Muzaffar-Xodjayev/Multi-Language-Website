from django.urls import path
from .views import *


urlpatterns = [
    path('',homepage, name='home-page'),
    path('about/',about, name='about-page'),
    path('contact/',contact, name='contact-page'),
    path('<slug:slug>',post_detail, name = 'post-detail-page'),
    path('signup/',signup, name='signup-page'),
]