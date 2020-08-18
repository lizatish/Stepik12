"""ask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include, re_path
from . import views
# from django.urls import path

urlpatterns = [
    url(r'^$', views.new_questions),
    # pathz(r'^/', views.new_questions),
    url('login/', views.test, name='login'),
    url('signup/', views.test, name='signup'),
    url(r'^question/(?P<id>[0-9]+)/$', views.question, name='question'),
    url('ask/', views.test, name='ask'),
    url('popular/', views.popular_questions, name='popular'),
    url('new/', views.test, name='new')
]
