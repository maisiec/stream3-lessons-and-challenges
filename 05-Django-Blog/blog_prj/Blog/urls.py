"""blog_prj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^blog/$', views.post_list, name='post_list'),
	url(r'^blog/(?P<id>\d+)/$', views.post_detail),
	url(r'^blog/top', views.top_posts),
    url(r'^post/new/$', views.new_post, name='new_post'),
    url(r'^blog/(?P<id>\d+)/edit$', views.edit_post, name='edit'),
]
