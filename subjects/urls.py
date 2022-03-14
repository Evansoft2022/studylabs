from django.conf.urls import url
from .views import *

urlpatterns=[
		url(r'^$',List_Courses,name="List_Courses"),
	]