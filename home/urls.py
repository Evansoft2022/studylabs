from django.conf.urls import url
from .views import *

urlpatterns=[
		url(r'^$',home,name="home"),
		url(r'^about/$',about,name="about"),
		url(r'^contact/$',contact,name="contact"),
	]