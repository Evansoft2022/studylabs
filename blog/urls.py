from django.conf.urls import url
from .views import *

urlpatterns=[
		url(r'^$',Blog,name="Blog"),
		url(r'^Single/$',Single,name="Single"),
	]