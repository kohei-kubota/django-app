from django.conf.urls import url
from app import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^detail/(?P<id>[0-9]+)/$', views.detail, name='detail'),
]
