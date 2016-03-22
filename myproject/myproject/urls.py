"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.models import User
from myblog.views import BlogListView, BlogDetailView, TagListView, TagDetailView, JsonResponseView, BlogCreateView, \
    RegisterUserView, LogoutView, TagCreateView, LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.edit import FormView
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = patterns('',
    # Examples:
    url(r'^$', BlogListView.as_view(), name='blog_list'),
    url(r'^blog/create/', login_required(BlogCreateView.as_view()), name='blog_create'),
    url(r'^tag/create/', login_required(TagCreateView.as_view()), name='tag_create'),
    url(r'^json-feed$', JsonResponseView.as_view(), name='json-feed'),
    url(r'^details/(?P<slug>[-_\w]+)/$', BlogDetailView.as_view(), name='blog_details'),
    url(r'^tags/details/(?P<pk>[0-9]+)/', TagDetailView.as_view(), name='tag_details'),
    url(r'^tags/$', TagListView.as_view(), name='tag_list'),
    url(r'^register/$', RegisterUserView.as_view(), name='register_user'),
    url(r'^logout/$', login_required(LogoutView.as_view()), name='logout_user'),
    url(r'^login/$', LoginView.as_view(), name='login_user'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls), name='admin-site'),

   )+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

