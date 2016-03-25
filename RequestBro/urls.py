"""RequestBro URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from djrequest import views, rest_api
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', rest_api.UserViewSet)
router.register(r'simpleusers', rest_api.UserSimpleViewSet)
router.register(r'userpref', rest_api.UserPrefViewSet)
router.register(r'songs', rest_api.SongViewSet)
router.register(r'songrequests', rest_api.SongRequestViewSet)
router.register(r'detailedsongrequests', rest_api.SongRequestDetailedViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^auth/', include('rest_framework_social_oauth2.urls')),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^$', views.Landing.as_view(), name='landing'),
    url(r'^accounts/login/$', views.LoginRedirect.as_view(pattern_name='landing')),
    url(r'^dev/$', 'djrequest.views.home'),
    url(r'^accounts/logout/$', 'djrequest.views.logout'),
    url(r'^accounts/logout/$', 'djrequest.views.logout'), #
    url(r'^accounts/(?P<username>[0-9A-Za-z_]{4,25})/$', views.Profile.as_view(), name='profile'),
    url(r'^accounts/update/simple/$', views.SimpleUpdateUser.as_view(), name='simpleupdate'),
    url(r'^done/$', 'djrequest.views.done', name='done'),
    url(r'^ajax-auth/(?P<backend>[^/]+)/$', 'djrequest.views.ajax_auth',
        name='ajax-auth'),
]
