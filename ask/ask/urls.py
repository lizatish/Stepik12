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
"""from django.urls import path, include, re_path"""
urlpatterns = [
    url(r'^$', include('qa.urls')),
    url(r'^login/', include('qa.urls'), name='login'),
    url(r'^signup/', include('qa.urls'), name='signup'),
    url(r'^question/(?P<id>[0-9]+)/$', include('qa.urls'), name='question'),
    url('^ask/', include('qa.urls'), name='ask'),
    url('^popular/', include('qa.urls'), name='popular'),
    url(r'^new/', include('qa.urls'), name='new')
]
